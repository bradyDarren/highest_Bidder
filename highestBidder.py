
# dictonary holds key value pairs input by the user
bidders = {"Tommy":101, "Carl": 102, "Darren": 120}

# accepts input from user and populates the bidder dictionary 
def bid():
    # more_bids = "yes"
    # while more_bids != "no":
    #     user_name = input("Enter your name: ")
    #     user_bid = input("Enter your desired bid amount: ")
    #     bidders[user_name] = user_bid
    #     print(bidders)
    #     more_bids = input("Are there any more bidders? Type 'yes or no'. ").lower()
    
    for key in bidders:
        max_bid = max(bidders)
        a = bidders.get("Tommy")
    print(max_bid)
    print(a)
          


bid()




