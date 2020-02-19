SELECT COUNT(*) as SellersNumber
FROM (SELECT DISTINCT u.UserID
FROM Items i, Users u
WHERE u.UserID = i.UserID
AND u.Rating > 1000);