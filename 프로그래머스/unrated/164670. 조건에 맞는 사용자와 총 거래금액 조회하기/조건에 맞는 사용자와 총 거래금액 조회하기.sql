-- 코드를 입력하세요
SELECT 
USER_ID,
NICKNAME,
concat(CITY, ' ', STREET_ADDRESS1, ' ', STREET_ADDRESS2) as "전체주소",
concat(left(TLNO,3), '-', substr(TLNO,4,4), '-', right(TLNO,4)) as "전화번호"

from USED_GOODS_BOARD as b
join USED_GOODS_USER as u on b.WRITER_ID = u.USER_ID

group by WRITER_ID
having count(WRITER_ID) >= 3
order by USER_ID desc