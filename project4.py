import random
print('You live in a pretty messy world, this world is limited in supplies and in clean water. Your job is to deliver supplies to the next city.')
totalsupplies = 50 
delivered = random.randint(10,82)
dayCount = 0 
trialnum = 0
while trialnum < 10000 :
    totalsupplies = 50
    while totalsupplies < 1000000 :
        totalsupplies += delivered
        dayCount += 1
    trialnum += 1    
print('total supplies:', totalsupplies)
print('total days:', dayCount)
print('total trials:', trialnum) 
print('Average number of days are :', dayCount/trialnum)       
