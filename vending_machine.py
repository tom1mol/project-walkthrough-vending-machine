from byotest import *                #from byotest import everything

def get_change(amount):
    if amount == 0:                 #amount = amount of money we ned to provide change for
        return []
     
    if amount in [100, 50, 20, 10, 5, 2, 1]:        #if statement protects existing tests
        return [amount]
    
    change = []
    for coin in [100, 50, 20, 10, 5, 2, 1]:
        if coin <= amount:                  #if coin value <= value we passed in..
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

print("All tests pass!")