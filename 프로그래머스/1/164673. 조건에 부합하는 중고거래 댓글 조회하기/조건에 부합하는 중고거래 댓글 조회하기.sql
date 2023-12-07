-- 코드를 입력하세요
SELECT B.TITLE, B.BOARD_ID, R.REPLY_ID, R.WRITER_ID, R.CONTENTS, 
DATE_FORMAT(R.CREATED_DATE,'%Y-%m-%d')
FROM USED_GOODS_BOARD AS B 
INNER JOIN USED_GOODS_REPLY AS R
ON R.BOARD_ID = B.BOARD_ID
WHERE YEAR(B.CREATED_DATE) = '2022'
AND MONTH(B.CREATED_DATE) = '10' 
ORDER BY R.CREATED_DATE, B.TITLE;
