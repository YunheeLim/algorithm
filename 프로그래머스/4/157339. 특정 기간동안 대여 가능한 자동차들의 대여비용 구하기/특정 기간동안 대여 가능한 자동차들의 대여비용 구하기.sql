SELECT 
    C.CAR_ID, 
    C.CAR_TYPE, 
    FLOOR(C.DAILY_FEE * (100 - D.DISCOUNT_RATE) * 0.01 * 30) AS FEE
FROM CAR_RENTAL_COMPANY_CAR C
JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN D
    ON C.CAR_TYPE = D.CAR_TYPE AND D.DURATION_TYPE = '30일 이상'
WHERE C.CAR_TYPE IN ('세단', 'SUV')
  AND NOT EXISTS (
      SELECT 1
      FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY H
      WHERE H.CAR_ID = C.CAR_ID
        AND H.START_DATE <= '2022-11-30'
        AND H.END_DATE >= '2022-11-01'
  )
  AND FLOOR(C.DAILY_FEE * (100 - D.DISCOUNT_RATE) * 0.01 * 30) >= 500000
  AND FLOOR(C.DAILY_FEE * (100 - D.DISCOUNT_RATE) * 0.01 * 30) < 2000000
ORDER BY FEE DESC, C.CAR_TYPE ASC, C.CAR_ID DESC;
