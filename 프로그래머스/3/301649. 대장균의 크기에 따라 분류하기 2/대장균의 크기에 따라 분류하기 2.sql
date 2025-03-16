SELECT ID,
    CASE
        WHEN D.R >= 0.75 THEN 'CRITICAL'
        WHEN D.R >= 0.5 THEN 'HIGH'
        WHEN D.R >= 0.25 THEN 'MEDIUM'
        ELSE 'LOW'
    END AS COLONY_NAME
FROM (SELECT ID, PERCENT_RANK() OVER (ORDER BY SIZE_OF_COLONY) AS R FROM ECOLI_DATA) D
ORDER BY ID
