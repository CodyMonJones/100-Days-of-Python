bids = {}

print("Welcome to the silent Auction!\n")

bidder_name = input("What is your name? ")
single_bid = int(input("How much would you like to bid? $"))

bids[bidder_name] = single_bid
highest_bid = 0
new_bid = True

while new_bid:
    new_bid_check = input("Is there another bidder? 'Yes' 'No'").lower()
    if new_bid_check == "yes":
        bidder_name = input("What is your name? ")
        single_bid = int(input("How much would you like to bid? $"))
        bids[bidder_name] = single_bid
        print(bids)
    else:
        new_bid = False    

for bid in bids:
    if bids[bid] > highest_bid:
        highest_bid = bids[bid]
print(f"The highest bid was {highest_bid} by {bid}")            