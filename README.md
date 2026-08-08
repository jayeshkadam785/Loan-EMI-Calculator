# Task 1: Loan EMI Calculator

**Internship:** Software Development | SaiKet Systems
**Language:** Python 3

## Objective
Develop a program to calculate the monthly installment (EMI) for a loan using the standard EMI formula.

## Formula Used
```
EMI = [P × R × (1+R)^N] / [(1+R)^N − 1]
```
Where:
- **P** = Principal loan amount
- **R** = Monthly interest rate (Annual Rate / 12 / 100)
- **N** = Loan tenure in months

## Features
- Interactive command-line input for Principal, Annual Interest Rate, and Tenure
- Handles zero-interest edge case
- Displays EMI, Total Payment, and Total Interest Payable
- Input validation (rejects non-numeric / invalid values)
- Option to run multiple calculations in one session

## How to Run
```bash
python emi_calculator.py
```

## Sample Output
```
Enter Principal Amount (₹): 500000
Enter Annual Interest Rate (%): 8.5
Enter Loan Tenure (months): 24

---------------------------------------------
RESULT
---------------------------------------------
Principal Amount   : ₹ 500,000.00
Annual Interest    : 8.50 %
Loan Tenure        : 24 months
---------------------------------------------
Monthly EMI        : ₹ 22,727.84
Total Payment      : ₹ 545,468.10
Total Interest     : ₹ 45,468.10
```

## Requirements
- Python 3.x (no external libraries needed)
