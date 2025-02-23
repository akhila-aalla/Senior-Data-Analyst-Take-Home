
-- What are the top 5 brands by receipts scanned among users 21 and over?
SELECT 
SELECT 
    p.brand, 
    COUNT(t.receipt_id) AS receipt_count
FROM transactions t
JOIN users u ON t.user_id = u.id
JOIN products p ON t.barcode = p.barcode
WHERE (strftime('%Y', 'now') - strftime('%Y', u.birth_date)) >= 21
GROUP BY p.brand
ORDER BY receipt_count DESC
LIMIT 5;

-- What are the top 5 brands by sales among users that have had their account for at least six months?
SELECT 
    p.brand, 
    SUM(t.sale) AS total_sales
FROM transactions t
JOIN users u ON t.user_id = u.id
JOIN products p ON t.barcode = p.barcode
WHERE u.created_date <= DATE('now', '-6 months')
GROUP BY p.brand
ORDER BY total_sales DESC
LIMIT 5;

-- What is the percentage of sales in the Health & Wellness category by generation?

SELECT 
    u.language, 
    SUM(t.sale) AS total_sales,
    SUM(CASE WHEN p.category_1 = 'Health & Wellness' THEN t.sale ELSE 0 END) AS health_wellness_sales,
    (SUM(CASE WHEN p.category_1 = 'Health & Wellness' THEN t.sale ELSE 0 END) / SUM(t.sale)) * 100 AS health_wellness_percentage
FROM transactions t
JOIN users u ON t.user_id = u.id
JOIN products p ON t.barcode = p.barcode
GROUP BY u.language
ORDER BY health_wellness_percentage DESC;