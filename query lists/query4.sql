SELECT ItemID
FROM(SELECT MAX(Items.Currently) as HighestPrice, Items.ItemID
FROM Items);