SELECT COUNT(*) as SellersNumber
FROM (SELECT DISTINCT u.UserID
FROM Items i, Users u
WHERE u.UserID = i.SellerID
AND u.Rating > 1000);