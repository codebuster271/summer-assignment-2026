-- PART A: CUSTOMER NODES EXPLORATION

-- Q1
SELECT COUNT(DISTINCT node_id) AS unique_nodes
FROM data_bank.customer_nodes;

-- Q2
SELECT 
    r.region_name, 
    COUNT(cn.node_id) AS node_count
FROM data_bank.customer_nodes cn
JOIN data_bank.regions r ON cn.region_id = r.region_id
GROUP BY r.region_name
ORDER BY node_count DESC;

-- Q3
SELECT 
    r.region_name, 
    COUNT(DISTINCT cn.customer_id) AS customer_count
FROM data_bank.customer_nodes cn
JOIN data_bank.regions r ON cn.region_id = r.region_id
GROUP BY r.region_name
ORDER BY customer_count DESC;

-- Q4
SELECT ROUND(AVG(end_date - start_date), 1) AS avg_reallocation_days
FROM data_bank.customer_nodes
WHERE end_date != '9999-12-31';

-- Q5
WITH reallocation_days AS (
    SELECT 
        r.region_name,
        (cn.end_date - cn.start_date) AS days
    FROM data_bank.customer_nodes cn
    JOIN data_bank.regions r ON cn.region_id = r.region_id
    WHERE cn.end_date != '9999-12-31'
)
SELECT 
    region_name,
    PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY days) AS median_days,
    PERCENTILE_CONT(0.8) WITHIN GROUP (ORDER BY days) AS percentile_80,
    PERCENTILE_CONT(0.95) WITHIN GROUP (ORDER BY days) AS percentile_95
FROM reallocation_days
GROUP BY region_name;


-- PART B: CUSTOMER TRANSACTIONS

-- Q1
SELECT 
    txn_type,
    COUNT(*) AS unique_count,
    SUM(txn_amount) AS total_amount
FROM data_bank.customer_transactions
GROUP BY txn_type;

-- Q2
WITH customer_deposits AS (
    SELECT 
        customer_id,
        COUNT(*) AS deposit_count,
        SUM(txn_amount) AS deposit_amount
    FROM data_bank.customer_transactions
    WHERE txn_type = 'deposit'
    GROUP BY customer_id
)
SELECT 
    ROUND(AVG(deposit_count), 1) AS avg_deposit_count,
    ROUND(AVG(deposit_amount), 1) AS avg_deposit_amount
FROM customer_deposits;

-- Q3
WITH monthly_activity AS (
    SELECT 
        customer_id,
        DATE_PART('month', txn_date) AS txn_month,
        SUM(CASE WHEN txn_type = 'deposit' THEN 1 ELSE 0 END) AS deposit_count,
        SUM(CASE WHEN txn_type = 'purchase' THEN 1 ELSE 0 END) AS purchase_count,
        SUM(CASE WHEN txn_type = 'withdrawal' THEN 1 ELSE 0 END) AS withdrawal_count
    FROM data_bank.customer_transactions
    GROUP BY customer_id, DATE_PART('month', txn_date)
)
SELECT 
    txn_month,
    COUNT(DISTINCT customer_id) AS customer_count
FROM monthly_activity
WHERE deposit_count > 1 
  AND (purchase_count >= 1 OR withdrawal_count >= 1)
GROUP BY txn_month
ORDER BY txn_month;