import requests
import json

r = requests.get("https://api.hypixel.net/skyblock/auctions").json
itemToBeFound = "Dirt"
auctions = r['auctions']

def main():
    for auction in auctions:
        if "auction" in auction:
            if itemToBeFound in auction['item_name']:
                f = open("hypixeldata2.txt", "a")
                f.writelines(auction['item_name'])
                starting_bid = str(auction['starting_bid'])
                f.writelines(starting_bid)
                f.writelines(auction['tier'])
                f.writelines("-----------------------------------------------------")
                f.close()