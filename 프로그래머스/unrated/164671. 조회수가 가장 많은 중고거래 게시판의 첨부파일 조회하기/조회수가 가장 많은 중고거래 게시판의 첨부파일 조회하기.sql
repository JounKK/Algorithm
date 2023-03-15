-- 코드를 입력하세요
SELECT
concat('/home/grep/src/',f.BOARD_ID,'/',f.FILE_ID,f.FILE_NAME,f.FILE_EXT) as FILE_PATH
# from USED_GOODS_BOARD as b
# join USED_GOODS_FILE as f
# on b.BOARD_ID = f.BOARD_ID
# having max(b.VIEWS)
# order by f.file_id desc

FROM(SELECT *
    FROM USED_GOODS_BOARD
    ORDER BY VIEWS DESC
    LIMIT 1) B
LEFT JOIN USED_GOODS_FILE F ON B.BOARD_ID = F.BOARD_ID
ORDER BY F.FILE_ID DESC