# SQL Mastery Assignment — Olist Dataset on PostgreSQL

## Objective

Practice real-world SQL using the Olist Brazilian E-Commerce dataset. This assignment is designed to build strong command over joins, aggregation, CTEs, window functions, ranking, date handling, business KPIs, and analytical thinking.

## Dataset Tables

Use these main tables:

- `orders`
- `order_items`
- `customers`
- `sellers`
- `products`
- `product_category_name_translation`
- `payments`
- `reviews`
- `geolocation`

---

# Part 1: Basic Data Understanding

1. Count total rows in each table.
2. Find the date range of orders.
3. Count total unique customers.
4. Count total unique sellers.
5. Count total unique products.
6. Find all unique order statuses.
7. Count orders by order status.
8. Find missing values in important columns like:
   - `order_approved_at`
   - `order_delivered_customer_date`
   - `order_estimated_delivery_date`
   - `product_category_name`

---

# Part 2: Joins Practice

9. Show each order with customer state.
10. Show each order item with product category.
11. Show each order item with seller state.
12. Show customer state, seller state, product category, price, and freight value together.
13. Find orders that have more than one item.
14. Find orders that contain products from more than one seller.
15. Find orders where customer state and seller state are different.

---

# Part 3: Aggregation and Business KPIs

16. Calculate total revenue using `price`.
17. Calculate total freight revenue.
18. Calculate total order value as `price + freight_value`.
19. Find revenue by product category.
20. Find revenue by customer state.
21. Find revenue by seller state.
22. Find top 10 products by revenue.
23. Find top 10 sellers by revenue.
24. Find average order value.
25. Find average freight value by state.
26. Find number of orders per customer.
27. Find customers with highest total spending.
28. Find sellers with highest number of orders.
29. Find category-wise average product price.
30. Find state-wise average order value.

---

# Part 4: Date and Time Analysis

31. Extract year, month, and day from order purchase timestamp.
32. Find monthly order count.
33. Find monthly revenue.
34. Find daily order count.
35. Find revenue by day of week.
36. Find order count by hour of day.
37. Find average delivery time in days.
38. Find average delivery time by customer state.
39. Find average delivery time by product category.
40. Find late deliveries where actual delivery date is greater than estimated delivery date.
41. Find late delivery percentage.
42. Find late delivery percentage by customer state.
43. Find late delivery percentage by seller state.

---

# Part 5: CTE Practice

44. Create a CTE for order-level revenue.
45. Use the CTE to find top 10 orders by revenue.
46. Use the CTE to calculate monthly revenue.
47. Use multiple CTEs to calculate category-wise revenue ranking.
48. Use CTEs to find customers whose total spending is above average.
49. Use CTEs to find sellers whose revenue is above average seller revenue.
50. Use CTEs to calculate late delivery percentage by state.

---

# Part 6: Window Functions

51. Rank customers by total spending within each state.
52. Find top 3 customers from each state.
53. Rank sellers by revenue.
54. Rank sellers by revenue within each product category.
55. Find top 5 sellers per category.
56. Calculate monthly running revenue.
57. Calculate running revenue per seller month by month.
58. Calculate each category’s percentage contribution to total revenue.
59. Calculate each seller’s percentage contribution to total revenue.
60. Compare each order value with average order value using window functions.
61. Find customer order sequence using `ROW_NUMBER()`.
62. Find first order and latest order of each customer.
63. Find repeat customers.
64. Find time gap between customer orders using `LAG()`.

---

# Part 7: Advanced Business Questions

65. Which product categories generate high revenue but have poor review scores?
66. Which states have high order volume but high late delivery percentage?
67. Which sellers have high revenue but low average review score?
68. Which categories have the highest freight cost compared to product price?
69. Which customers are high-value repeat customers?
70. Which sellers are most dependent on a single product category?
71. Which states have the highest average delivery delay?
72. Which product categories are most affected by late delivery?
73. Find customer states where average order value is above the overall average.
74. Find seller states where late delivery rate is above the overall late delivery rate.
75. Find the relationship between review score and delivery delay.

---

# Part 8: Payment Analysis

76. Count orders by payment type.
77. Find revenue by payment type.
78. Find average payment installments by payment type.
79. Find payment type preference by customer state.
80. Find customers who used more than one payment type.
81. Find average order value by payment type.
82. Find payment types with highest review score.

---

# Part 9: Review Analysis

83. Count reviews by review score.
84. Find average review score.
85. Find average review score by product category.
86. Find average review score by seller.
87. Find average review score by customer state.
88. Find categories with average review score below 4.
89. Find sellers with average review score below 4 and more than 50 orders.
90. Find late delivery impact on review score.

---

# Part 10: Final Capstone Queries

91. Build a seller performance report with:

- seller_id
- seller_state
- total_orders
- total_revenue
- average_review_score
- late_delivery_percentage

92. Build a product category performance report with:

- category name
- total_orders
- total_revenue
- average_price
- average_freight
- average_review_score
- late_delivery_percentage

93. Build a customer state performance report with:

- customer_state
- total_orders
- total_customers
- total_revenue
- average_order_value
- average_delivery_time
- late_delivery_percentage

94. Find the top 10 best overall sellers based on revenue, review score, and delivery performance.

95. Find the worst 10 sellers based on low review score and high late delivery percentage.

---

# Bonus Challenge

Create a final SQL view named:

```sql
seller_performance_summary
```

It should include:

- seller_id
- seller_state
- total_orders
- total_items_sold
- total_revenue
- average_order_value
- average_review_score
- average_delivery_days
- late_delivery_percentage
- seller_rank_by_revenue

---

# Submission Requirement

For each question, submit:

1. SQL query
2. Output screenshot or result table
3. Short business interpretation

Example:

```text
Business Insight:
São Paulo generated the highest revenue, which means it is the strongest customer market in the dataset.
```

---

# Skills Covered

By completing this assignment, you will practice:

- SELECT queries
- Filtering
- GROUP BY
- HAVING
- INNER JOIN
- LEFT JOIN
- CTEs
- Subqueries
- Window functions
- Ranking
- Date functions
- Business KPI creation
- Analytical SQL thinking
