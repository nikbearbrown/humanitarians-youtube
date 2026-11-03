---
type: Metric
title: Revenue
description: How revenue is calculated.
tags: [sales, finance]
generated: { by: human:likhith, at: 2026-10-22T09:00:00-04:00 }
---
Revenue is the sum of `amount` over [orders](../tables/orders.md)
with `status = paid`. Refunded orders are excluded; see
[refunds](../policies/refunds.md).
