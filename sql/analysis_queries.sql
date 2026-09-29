USE ecommerce_analytics;
-- Monthly sales and profit
SELECT DATE_FORMAT(order_date,'%Y-%m') month, SUM(sales) sales,
       SUM(sales-cost) profit, COUNT(DISTINCT order_id) orders
FROM orders GROUP BY DATE_FORMAT(order_date,'%Y-%m') ORDER BY month;
-- Category mix
SELECT category, SUM(sales) revenue, SUM(sales-cost) profit
FROM orders GROUP BY category ORDER BY revenue DESC;
-- State performance
SELECT state, SUM(sales) revenue, COUNT(DISTINCT order_id) orders
FROM orders GROUP BY state ORDER BY revenue DESC;
