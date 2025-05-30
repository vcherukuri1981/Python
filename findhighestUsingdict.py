# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

def find_highest_bidder(bids):
    winner = ""
    highest_bid = 0
    for dict_name, bid_amount in bids.items():
        if bid_amount>highest_bid:
            highest_bid=bid_amount
            winner=dict_name
    print(f"The winner is {winner} with a bid of ${highest_bid}")


bid={}
continue_bidding = True

while continue_bidding:
    name = input("What is your name?:")
    price = int(input("What is your bid?:"))
    bid[name]=price
    should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bid)
        print("Thank you for bidding!")
    elif should_continue == "yes":
        print("\n" * 20)


   

