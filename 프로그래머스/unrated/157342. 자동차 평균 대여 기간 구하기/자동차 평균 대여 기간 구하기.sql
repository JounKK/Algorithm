-- 코드를 입력하세요
SELECT CAR_ID, 
ROUND(AVG(DATEDIFF(END_DATE,START_DATE)+1),1) as AVERAGE_DURATION
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
group by CAR_ID
having AVERAGE_DURATION >= 7
ORDER BY AVERAGE_DURATION DESC, CAR_ID DESC
