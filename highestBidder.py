

bidders = {}

def bid():
    more_bids = "yes"
    while more_bids != "no":
        user_name = input("Enter your name: ")
        user_bid = int(input("Enter your desired bid amount: "))
        bidders[user_name] = user_bid
        print(bidders)
        more_bids = input("Are there any more bidders? Type 'yes or no'. ").lower()
    
    for key in bidders:
        max_bid = max(bidders[key])
    print(max_bid)
        



bid()




