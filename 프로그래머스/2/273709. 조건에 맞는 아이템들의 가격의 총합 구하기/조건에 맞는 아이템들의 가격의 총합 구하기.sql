SELECT SUM(PRICE) AS TOTAL_PRICE FROM ITEM_INFO
WHERE ITEM_ID IN (SELECT ITEM_ID FROM ITEM_INFO WHERE RARITY = 'LEGEND')