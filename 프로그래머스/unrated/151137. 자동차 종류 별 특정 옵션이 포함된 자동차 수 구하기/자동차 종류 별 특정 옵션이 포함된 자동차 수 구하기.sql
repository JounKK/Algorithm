-- 코드를 입력하세요
SELECT CAR_TYPE, 
count(CAR_ID) as CARS
FROM CAR_RENTAL_COMPANY_CAR
WHERE REGEXP_LIKE(OPTIONS, '통풍시트|열선시트|가죽시트')
Group by CAR_TYPE
Order by CAR_TYPE