# build a blind bidding game 


auction = {}
continue_bidding = True
while continue_bidding:
    name = input("what is your name?: ")
    bid_amount= int(input("what is your bid amount?: $"))
    auction[name] = bid_amount
    should_continue = input("Type 'yes' for another person to bid or 'no' to stop bidding\n").lower()

    if should_continue == "yes":
        #clear the screen 
            print("\n" * 20)

    elif should_continue == "no":
        continue_bidding = False
        highest_amount= 0
        for key in auction:
            amount_bidded = auction[key]

            if amount_bidded > highest_amount:
                highest_amount = amount_bidded

        print(f"The winner of this auction is {key} with ${highest_amount}")

