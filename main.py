import os

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)


silent_auction_bid = {}
keep_bidding = False


def highest_bidder(bid_record):
    highest_bidder_bid = 0
    winner = ""
    for bidder in bid_record:
        bid_amount = bid_record[bidder]
        if bid_amount > highest_bidder_bid:
            highest_bidder_bid = bid_amount
            winner = bidder
    print(f"{name} is the Winner, with a bid of ${highest_bidder_bid}")


while not keep_bidding:
    name = input("What is your name? : ")
    bid_amount = int(input("How much will you bid? : $"))
    os.system('cls')
    silent_auction_bid[name] = bid_amount
    continue_bidding = input("Are there any other bidders? 'Y' or 'N' : \n").lower()
    if continue_bidding == 'n':
        keep_bidding = True
        highest_bidder(silent_auction_bid)
    elif continue_bidding == 'y':
        os.system('cls')

print(silent_auction_bid)
