def simple_interest(p,t,r):
    print('Principal Amount: ', p)
    print('Time Period: ', t)
    print('Rate of Interest: ',r)

    si = (p * t * r)/100

    print('The Simple Interest is', si)

def compound_interest(principle, rate, time):

    # Calculates compound interest
    Amount = principle * (pow((1 + rate / 100), time))
    CI = Amount - principle
    print("Compound interest is", CI)

print("Interest Finder")

principleAmount = int(input("Enter the principal Amount:" ))
timePeriod = float(input("Enter Time Period:" ))
interest = float(input("Enter the percentage of interest:" ))
choice = int(input("Choose one:\n1. Simple Interest\n2. Compound Interest "))
if choice == 1:
    simple_interest(principleAmount,timePeriod,interest)
if choice == 2:
    rate = float(input("Enter rate: "))
    compound_interest(principleAmount,rate,timePeriod)
