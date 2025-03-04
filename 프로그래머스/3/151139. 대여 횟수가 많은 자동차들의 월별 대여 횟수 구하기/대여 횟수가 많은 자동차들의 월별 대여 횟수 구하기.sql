# SELECT MONTH(START_DATE) AS MONTH, CAR_ID, COUNT(HISTORY_ID) AS RECORDS
# FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
# WHERE START_DATE >= '2022-08-01' AND END_DATE < '2022-11-01'
# AND CAR_ID IN
# (SELECT CAR_ID FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY WHERE START_DATE >= '2022-08-01' AND END_DATE < '2022-11-01' GROUP BY CAR_ID HAVING COUNT(CAR_ID) >= 5)
# GROUP BY MONTH, CAR_ID
# HAVING RECORDS > 0
# ORDER BY MONTH ASC, CAR_ID DESC

SELECT month(start_date) as month, car_id, count(history_id) as records
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where start_date>="2022-08-01" and start_date<"2022-11-01" and car_id in (select car_id from CAR_RENTAL_COMPANY_RENTAL_HISTORY where start_date>="2022-08-01" and start_date<"2022-11-01" group by car_id having count(history_id)>4) 
group by month, car_id
having records >0
order by month, car_id desc