SELECT COUNT(*) as CategoriesNumber
FROM (SELECT DISTINCT c.Name
FROM Categories c, Items i, Bids b
WHERE c.ItemID = i.ItemID
AND i.ItemID = b.ItemID
AND b.Amount > 100);