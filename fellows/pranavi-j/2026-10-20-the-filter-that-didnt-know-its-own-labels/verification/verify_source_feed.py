"""
Live verification harness for the source_feed fix (feeds.py commit 565e84e).
Mounts the REAL feeds.py router from the mycroft repo (post-fix state, current
working tree) behind a FastAPI TestClient, with FeedCRUD.list_feeds mocked out
(no live DB needed) so we can confirm:
  1. A dynamic classifier label ("Federal Register - Department of Labor") now
     passes query-param validation and reaches the (mocked) CRUD function.
  2. A known-good fixed-enum label still works unchanged.
  3. Re-running the SAME request against the PRE-FIX router definition (the
     Optional[SourceFeed] enum) reproduces the real 422 this bug caused.
"""
import sys
from unittest.mock import patch

sys.path.insert(0, "/Users/pranavijs/mycroft/scripts/mycroft-main/Core_Components/Regulatory_QA/backend")

from fastapi import FastAPI
from fastapi.testclient import TestClient

DYNAMIC_LABEL = "Federal Register - Department of Labor"
FIXED_LABEL = "SEC Press Releases"

MOCK_RESULT = {
    "feeds": [],
    "total": 0,
    "limit": 50,
    "offset": 0,
    "filters_applied": {},
}

def run_post_fix():
    from app.routers import feeds as feeds_router
    app = FastAPI()
    app.include_router(feeds_router.router)
    client = TestClient(app)

    with patch.object(feeds_router.FeedCRUD, "list_feeds", return_value=MOCK_RESULT) as mocked:
        r_dynamic = client.get("/api/feeds/list", params={"source_feed": DYNAMIC_LABEL})
        call_args_dynamic = mocked.call_args.kwargs.get("source_feed") if mocked.call_args else None
        mocked.reset_mock()
        r_fixed = client.get("/api/feeds/list", params={"source_feed": FIXED_LABEL})
        call_args_fixed = mocked.call_args.kwargs.get("source_feed") if mocked.call_args else None

    print("=== POST-FIX (current working tree, commit 565e84e) ===")
    print(f"dynamic label {DYNAMIC_LABEL!r} -> status {r_dynamic.status_code}, "
          f"CRUD received source_feed={call_args_dynamic!r}")
    print(f"fixed  label {FIXED_LABEL!r} -> status {r_fixed.status_code}, "
          f"CRUD received source_feed={call_args_fixed!r}")
    return r_dynamic.status_code, call_args_dynamic, r_fixed.status_code, call_args_fixed


def run_pre_fix():
    # Reconstruct the PRE-FIX endpoint signature exactly as it was before
    # 565e84e (Optional[SourceFeed] enum, .value accessor) and mount it in an
    # isolated FastAPI app, to reproduce the real 422 without needing to git
    # checkout the parent commit.
    from fastapi import APIRouter, Query
    from typing import Optional, List
    from datetime import datetime
    from app.models import SourceFeed, ImpactLevel, FeedListResponse
    from app.routers.feeds import FeedCRUD

    router = APIRouter(prefix="/api/feeds", tags=["feeds"])

    @router.get("/list", response_model=FeedListResponse)
    async def list_feeds_prefix(
        source_feed: Optional[SourceFeed] = None,
        min_urgency: Optional[int] = Query(None, ge=1, le=10),
        max_urgency: Optional[int] = Query(None, ge=1, le=10),
        impact_level: Optional[ImpactLevel] = None,
        categories: Optional[List[str]] = Query(None),
        is_enforcement: Optional[bool] = None,
        has_deadline: Optional[bool] = None,
        date_from: Optional[datetime] = None,
        date_to: Optional[datetime] = None,
        limit: int = Query(50, ge=1, le=100),
        offset: int = Query(0, ge=0),
    ):
        result = FeedCRUD.list_feeds(
            source_feed=source_feed.value if source_feed else None,
            min_urgency=min_urgency, max_urgency=max_urgency,
            impact_level=impact_level.value if impact_level else None,
            categories=categories, is_enforcement=is_enforcement,
            has_deadline=has_deadline, date_from=date_from, date_to=date_to,
            limit=limit, offset=offset,
        )
        return FeedListResponse(**result)

    app = FastAPI()
    app.include_router(router)
    client = TestClient(app)

    with patch.object(FeedCRUD, "list_feeds", return_value=MOCK_RESULT) as mocked:
        r_dynamic = client.get("/api/feeds/list", params={"source_feed": DYNAMIC_LABEL})
        r_fixed = client.get("/api/feeds/list", params={"source_feed": FIXED_LABEL})

    print("\n=== PRE-FIX (reconstructed Optional[SourceFeed] signature, matches parent of 565e84e) ===")
    print(f"dynamic label {DYNAMIC_LABEL!r} -> status {r_dynamic.status_code}")
    if r_dynamic.status_code == 422:
        print(f"  body: {r_dynamic.json()}")
    print(f"fixed  label {FIXED_LABEL!r} -> status {r_fixed.status_code}")
    return r_dynamic.status_code, r_fixed.status_code


if __name__ == "__main__":
    post = run_post_fix()
    pre = run_pre_fix()
    print("\n=== SUMMARY ===")
    assert post[0] == 200, "post-fix dynamic label should pass (200)"
    assert post[1] == DYNAMIC_LABEL, "post-fix CRUD should receive the raw dynamic string"
    assert post[2] == 200, "post-fix fixed label should still pass (200)"
    assert pre[0] == 422, "pre-fix dynamic label should 422 (this is the bug)"
    assert pre[1] == 200, "pre-fix fixed label should still pass (enum covers it)"
    print("ALL ASSERTIONS PASSED:")
    print(f"  pre-fix  dynamic label -> {pre[0]} (422, bug reproduced)")
    print(f"  post-fix dynamic label -> {post[0]} (200, fix confirmed), CRUD got raw string {post[1]!r}")
    print(f"  fixed-enum label unaffected in both: pre {pre[1]}, post {post[2]}")
