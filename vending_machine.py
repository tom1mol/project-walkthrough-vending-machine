from byotest import *                #from byotest import everything

usd_coins = [100, 50, 25, 10, 5, 1]
eur_coins = [100, 50, 20, 10, 5, 2, 1]

def get_change(amount, coins=eur_coins): # equal sign means will default to eur_coins unless we supply argument(usd)
    """
    Takes the payment amount and returns the change
    `amount` the amount of money that we need to provide change for
    `coins` is the set of coins that we need to get change for (i.e. the set
        of available coins)
    Returns a list of coin values
    """
   
    
    change = []
    for coin in coins:
        while coin <= amount:                  #if coin value <= value we passed in..
                                            #while coin <= amount..keep adding until it isnt. then move on or rtn change
            amount -= coin                  #deduct amount of coin from amount we sent in
            change.append(coin)             #add that onto our change
    return change                           #return change list

test_are_equal(get_change(0),[])        #amount of change required =0..no coins back. 0 change get back empty list[]
test_are_equal(get_change(1),[1])
test_are_equal(get_change(2),[2])
test_are_equal(get_change(5), [5])
test_are_equal(get_change(10), [10])
test_are_equal(get_change(20), [20])
test_are_equal(get_change(50), [50])
test_are_equal(get_change(100), [100])
test_are_equal(get_change(3),[2,1])
test_are_equal(get_change(7),[5,2])
test_are_equal(get_change(9),[5,2,2])
test_are_equal(get_change(35, usd_coins),[25,10])

print("All tests pass!")