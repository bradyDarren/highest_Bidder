
# dictonary holds key value pairs input by the user
bidders = {}


# accepts input from user and populates the bidder dictionary 
def bid():
    more_bids = "yes"
    while more_bids != "no":
        user_name = input("Enter your name: ")
        user_bid = input("Enter your desired bid amount: ")
        bidders[user_name.strip()] = user_bid.strip()
        print(bidders)
        more_bids = input("Are there any more bidders? Type 'yes or no'. ").lower()
    return bidders 

final_list = bid()

# find the max value within the created dictionary.
def results(bidder_list):
    for key in bidder_list:
        max_bidder = max(bidder_list, key = bidder_list.get)
        max_bid = bidder_list[max_bidder]
    return f"Sold to {max_bidder} for the price of ${max_bid}."


print(results(final_list))

