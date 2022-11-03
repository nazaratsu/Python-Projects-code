"""
Create a Python program that calculates investment gain a user will get at the end of the investment term.

By Brandon Tuttle
8/23/22
"""
#call function  getInvestmentInfo to get invested amount, invested term in years, and investment annual interest rate
def main():
    info = get_investment_info()
    calcInvestment(info)

#Ask user enter invested amount, invested years, and apr, cast them in reasonable data type, and returns them back to caller.
def get_investment_info():
    principle = float(input("Investment Amount: "))
    apr = float(input("Enter your Interest Rate "))
    term = float(input("Enter your Loan Term "))
    return principle, apr, term


def calcInvestment(info):
    principle = info[0]
    apr = info[1]
    term = info[2]

#Received invested amount, invested years, and apr from caller
    future_value = principle * (1 + apr / 12 )**(term * 12)
    total_interest_earned = future_value - principle
    DisplayInfo(future_value, total_interest_earned, principle, apr, term)

#Display Principle, invested amount, and term
def DisplayInfo(future_value,total_interest_earned, principle, apr, term):
    print("Future Value: ", future_value)
    print("Total Interest Earned: ", total_interest_earned)
    print("Principle: ", principle,"Apr: ", apr, "Term: ", term)
main()
