user_input = input("Enter Your Name: ")

number_hours = float(input("Enter the number of hours you worked this week: "))

pay_rate = float(input("Enter your hourly pay rate: "))

gross_pay = number_hours * pay_rate

federal_tax = 0.20

state_tax = 0.09

gross_fed = gross_pay * federal_tax

gross_state = gross_pay * state_tax

gross_amount = gross_pay - gross_fed - gross_state

print("The Gross Pay is ", gross_pay)

print("The Federal tax on the gross payment ", gross_fed)

print("The State tax on the gross payment",gross_state)

print("The paid amount ",gross_amount)


