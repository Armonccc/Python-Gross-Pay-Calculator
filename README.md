# Gross Pay & Tax Calculator (Python)

This project is a simple Python program that calculates an employee’s weekly gross pay, federal tax, state tax, and final take-home pay based on user input. It was created as a beginner-friendly exercise in Python variables, user input, and arithmetic operations.

# Features
- Prompts the user to enter:
  - Name
  - Hours worked in the week
  - Hourly pay rate
- Calculates:
  - Gross pay
  - Federal tax (20%)
  - State tax (9%)
  - Final amount paid after taxes
- Displays a full payroll breakdown

# Example Calculation
The program uses:
- **Federal tax rate:** 20%
- **State tax rate:** 9%

```python
gross_pay = hours * pay_rate
federal_tax = gross_pay * 0.20
state_tax = gross_pay * 0.09
net_pay = gross_pay - federal_tax - state_tax
