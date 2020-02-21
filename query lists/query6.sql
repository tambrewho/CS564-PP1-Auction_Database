SELECT COUNT(*) as SameNumbers
FROM(SELECT DISTINCT i.SellerID
FROM Items i, Bids b
WHERE i.SellerID = b.BidderID);