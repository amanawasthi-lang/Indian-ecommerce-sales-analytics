CREATE DATABASE IF NOT EXISTS ecommerce_analytics;
USE ecommerce_analytics;
CREATE TABLE orders (
 order_id VARCHAR(30) PRIMARY KEY, order_date DATE, state VARCHAR(80),
 category VARCHAR(80), product VARCHAR(120), quantity INT,
 unit_price DECIMAL(12,2), discount_rate DECIMAL(5,4),
 sales DECIMAL(14,2), cost DECIMAL(14,2), channel VARCHAR(40), payment_method VARCHAR(40)
);
