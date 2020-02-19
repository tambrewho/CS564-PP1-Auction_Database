SELECT COUNT(*) as SameNumbers
FROM(SELECT DISTINCT i.UserID
FROM Items i, Bids b
WHERE i.UserID = b.UserID);