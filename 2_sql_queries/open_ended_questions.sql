-- Who are Fetch’s power users?
-- Assumption: Power users are defined as users with the highest number of transactions.
SELECT 
    t.user_id, 
    COUNT(t.receipt_id) AS transaction_count,
    SUM(t.sale) AS total_spent
FROM transactions t
GROUP BY t.user_id
ORDER BY transaction_count DESC
LIMIT 10;

-- Which is the leading brand in the Dips & Salsa category?
-- Assumption: The leading brand is determined by the highest sales in the 'Dips & Salsa' category.
SELECT 
    p.brand, 
    SUM(t.sale) AS total_sales
FROM transactions t
JOIN products p ON t.barcode = p.barcode
WHERE p.category_1 = 'Dips & Salsa'
GROUP BY p.brand
ORDER BY total_sales DESC
LIMIT 1;

--  At what percent has Fetch grown year over year?
-- Assumption: Growth is measured by the percentage increase in the number of users year over year.
SELECT 
    strftime('%Y', u.created_date) AS year,
    COUNT(u.id) AS total_users,
    (COUNT(u.id) - LAG(COUNT(u.id)) OVER (ORDER BY strftime('%Y', u.created_date))) * 100.0 / 
    LAG(COUNT(u.id)) OVER (ORDER BY strftime('%Y', u.created_date)) AS yoy_growth_percentage
FROM users u
GROUP BY year
ORDER BY year;