"""
FILE: my_parser.py
------------------
Author: Jiaru Fu (jfu57@wisc.edu)
Author: Yuren Sun (ysun299@wisc.edu)
Author: Tambre Hu (thu53@wisc.edu)
Course: CS 564
File Name: parser_modified.py
Professor: Paris Koutris
Due Date: 02/21/20

Skeleton parser for CS564 programming project 1.
"""

import sys
from json import loads
from re import sub

columnSeparator = "|"

# Dictionary of months used for date transformation
MONTHS = {'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04', 'May': '05', 'Jun': '06', \
          'Jul': '07', 'Aug': '08', 'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12'}

"""
Returns true if a file ends in .json
"""


def isJson(f):
    return len(f) > 5 and f[-5:] == '.json'


"""
Converts month to a number, e.g. 'Dec' to '12'
"""


def transformMonth(mon):
    if mon in MONTHS:
        return MONTHS[mon]
    else:
        return mon


"""
Transforms a timestamp from Mon-DD-YY HH:MM:SS to YYYY-MM-DD HH:MM:SS
"""


def transformDttm(dttm):
    dttm = dttm.strip().split(' ')
    dt = dttm[0].split('-')
    date = '20' + dt[2] + '-'
    date += transformMonth(dt[0]) + '-' + dt[1]
    return date + ' ' + dttm[1]


"""
Transform a dollar value amount from a string like $3,453.23 to XXXXX.xx
"""


def transformDollar(money):
    if money == None or len(money) == 0:
        return money
    return sub(r'[^\d.]', '', money)


"""
Parses a single json file. Currently, there's a loop that iterates over each
item in the data set. Your job is to extend this functionality to create all
of the necessary SQL tables for your database.
"""


def parseJson(json_file):
    with open(json_file, 'r') as f:
        items = loads(f.read())['Items']  # creates a Python dictionary of Items for the supplied json file

        # files to store the parsed data
        itemFile = open('items.dat', 'a')
        cateFile = open('categories.dat', 'a')
        bidsFile = open('bids.dat', 'a')
        usersFile = open('users.dat', 'a')

        temp_list = []

        for item in items:
            """
            TODO: traverse the items dictionary to extract information from the
            given `json_file' and generate the necessary .dat files to generate
            the SQL tables based on your relation design
            """
            # for all files, replace 123|29" bike rims|California|Bike rims that are 29"
            # to format as 123|"29"" bike rims"|"California"|"Bike rims that are 29"""
            # store value none as NULL

            # for itmes file
            itemFile.write(item['ItemID'] + "|")
            itemFile.write('\"' + item['Name'].replace('\"', '\"\"') + "\"|")

            itemFile.write(transformDollar(item['Currently']) + "|")
            # may not have the buy price
            try:
                itemFile.write(transformDollar(item['Buy_Price']) + '|')
            except KeyError:
                itemFile.write("NULL" + '|')
            itemFile.write(transformDollar(item['First_Bid']) + '|')

            itemFile.write(item['Number_of_Bids'] + '|')

            itemFile.write(transformDttm(item['Started']) + '|')
            itemFile.write(transformDttm(item['Ends']) + '|')
            itemFile.write('\"' + item['Seller']['UserID'].replace('\"', '\"\"') + '\"|')
            if item['Description']:
                itemFile.write('\"' + item['Description'].replace('\"', '\"\"') + '\"\n')
            else:
                itemFile.write('NULL \n')

            # for category file
            for category in item['Category']:
                cateFile.write('\"' + category.replace('\"', '\"\"') + '\"|')
                cateFile.write(item['ItemID'] + '\n')

            # for bids file
            if item['Bids']:
                for bid in item['Bids']:
                    bidsFile.write(item['ItemID'] + '|')
                    bidsFile.write('\"' + bid['Bid']['Bidder']['UserID'].replace('\"', '\"\"') + '\"|')
                    bidsFile.write(transformDttm(bid['Bid']['Time']) + '|')
                    bidsFile.write(transformDollar(bid['Bid']['Amount']) + '\n')
                    
                    #for user file
                    usersFile.write('\"' + bid['Bid']['Bidder']['UserID'].replace('\"', '\"\"') + '\"|')
                    usersFile.write(bid['Bid']['Bidder']['Rating'] + '|')
                    if 'Location' in bid['Bid']['Bidder'].keys():
                        usersFile.write('\"' + bid['Bid']['Bidder']['Location'].replace('\"', '\"\"') + '\"|')
                    else:
                        usersFile.write('NULL'+ '|')
                    if 'Country' in bid['Bid']['Bidder'].keys():
                        usersFile.write('\"' + bid['Bid']['Bidder']['Country'] + '\"\n')
                    else:
                        usersFile.write('NULL' + '\n')

            #for user file
            usersFile.write('\"' + item['Seller']['UserID'].replace('\"', '\"\"') + '\"|')
            usersFile.write(item['Seller']['Rating'] + '|')
            usersFile.write('\"' + item['Location'].replace('\"', '\"\"') + '\"|')
            usersFile.write('\"' + item['Country'].replace('\"', '\"\"') + '\"\n')

        itemFile.close()
        cateFile.close()
        bidsFile.close()
        usersFile.close()


"""
Loops through each json files provided on the command line and passes each file
to the parser
"""


def main(argv):
    if len(argv) < 2:
        print >> sys.stderr, 'Usage: python skeleton_json_parser.py <path to json files>'
        sys.exit(1)
    # loops over all .json files in the argument
    for f in argv[1:]:
        if isJson(f):
            parseJson(f)
            print("Success parsing " + f)


if __name__ == '__main__':
    main(sys.argv)
