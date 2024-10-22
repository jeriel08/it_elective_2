# Week 2 Let's Analyze 2

# Problem Scenario 1
print("Problem Scenario 1\n")
lender_name = input("Enter Lender Name: ")
principal_amount = float(input("Enter Principal Amount: "))
interest_rate = float(input("Enter Interest Rate per Annum: "))

processing_fee = principal_amount * 0.05
loanable_amount =  principal_amount - processing_fee
monthly_amortization = ((principal_amount * interest_rate) + principal_amount) / 12

print("---------------------------------------------")
print(f"Name of Lender       : {lender_name}")
print(f"Principal Amount     : {principal_amount:,.2f}")
print(f"5% Processing Fee    : {processing_fee:,.2f}")
print(f"Loanable Amount      : {loanable_amount:,.2f}")
print(f"Monthly Amortization : {monthly_amortization:,.2f}")
print("---------------------------------------------\n")

# Problem Scenario 2
print("Problem Scenario 2\n")
investor_name = input("Enter Investor Name: ")
capital = float(input("Enter Capital of Investment: "))

interest_per_month = capital * 7 # 700 / 100 = 7
monthly_payout = capital + interest_per_month
processing_fee_2 = monthly_payout * 0.015 # 1.5 / 100 = 0.015
net_income_per_month = monthly_payout - processing_fee_2
annual_interest = interest_per_month * 12
net_income_per_year = net_income_per_month * 12

print("---------------------------------------------")
print(f"Investor              : {investor_name}")
print(f"Capital               : {capital:,.2f}")
print(f"Month Interest        : {interest_per_month:,.2f}")
print(f"Processing Fee        : {processing_fee_2:,.2f}")
print(f"Monthly Payout        : {monthly_payout:,.2f}")
print(f"Net Income in a Month : {net_income_per_month:,.2f}")
print(f"Annual Interest       : {annual_interest:,.2f}")
print(f"Net Income in a Year  : {net_income_per_year:,.2f}")
print("---------------------------------------------")