---
type: Table
title: Orders
description: One row per completed customer order.
tags: [sales]
generated: { by: human:likhith, at: 2026-10-22T09:00:00-04:00 }
---
# Schema

| Column | Type | Description |
|---|---|---|
| `order_id` | STRING | Unique order id. |
| `customer_id` | STRING | Joins to [customers](customers.md). |
| `amount` | NUMERIC | Order total in USD. |
| `status` | STRING | `paid` or `refunded`. |
