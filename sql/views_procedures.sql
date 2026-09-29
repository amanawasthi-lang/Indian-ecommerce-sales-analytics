USE ecommerce_analytics;
CREATE OR REPLACE VIEW monthly_performance AS
SELECT DATE_FORMAT(order_date,'%Y-%m') month, SUM(sales) sales,
SUM(sales-cost) profit, COUNT(DISTINCT order_id) orders
FROM orders GROUP BY DATE_FORMAT(order_date,'%Y-%m');
DELIMITER //
CREATE PROCEDURE GetCategoryPerformance()
BEGIN
 SELECT category, SUM(sales) sales, SUM(sales-cost) profit
 FROM orders GROUP BY category ORDER BY sales DESC;
END//
DELIMITER ;
