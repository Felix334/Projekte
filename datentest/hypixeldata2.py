import requests

r = requests.get("https://api.hypixel.net/skyblock/auctions").json
item_found = "Dirt"

auctions = r['auctions']

for auction in auctions:
    if "auction" in auctions:
        if item_found in auction['item_name']:
            f = open("hypixeldata2.txt", "a")
            item_found = auction['item_name']
            starting_bid = auction['starting_bid']
            tier = auction['tier']
            f.writelines(item_found)
            starting_bid_int = starting_bid
            f.writelines(starting_bid_int)
            f.writelines(tier)
            f.writelines("-----------------------------------------------------")
            f.close()