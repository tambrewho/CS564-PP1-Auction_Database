python my_parser.py ebay_data/items-*.json

sort bids.dat | uniq > bids_sorted.dat
sort categories.dat | uniq > categories_sorted.dat
sort items.dat | uniq > items_sorted.dat
sort users.dat | uniq > users_sorted.dat
