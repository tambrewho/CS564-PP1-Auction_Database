SELECT COUNT(*) as AuctionNumber
FROM(SELECT COUNT(c.Name) as count
FROM Items i, Categories c
WHERE i.ItemID = c.ItemID
GROUP BY c.ItemID) as a
WHERE a.count = 4