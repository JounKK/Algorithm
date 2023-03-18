-- 코드를 입력하세요
SELECT distinct car.CAR_ID
from CAR_RENTAL_COMPANY_CAR as car
join CAR_RENTAL_COMPANY_RENTAL_HISTORY as h
on car.CAR_ID = h.CAR_ID
where car.CAR_TYPE = '세단' AND START_DATE between '2022-10-01' and '2022-10-31'
order by CAR_ID DESC

