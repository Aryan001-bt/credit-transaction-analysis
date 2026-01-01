SELECT txn_type, SUM(txn_amount)
FROM transactions
GROUP BY txn_type;

SELECT
 (SUM(DECODE(txn_status,'FAILED',1,0))*100)/COUNT(*) AS failed_percentage
FROM transactions;