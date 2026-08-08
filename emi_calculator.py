"""
Task 1: Loan EMI Calculator
SaiKet Systems - Software Development Internship

Formula: EMI = P * R * (1+R)^N / ((1+R)^N - 1)
P = Principal amount
R = Monthly interest rate (annual rate / 12 / 100)
N = Number of months (loan tenure)
"""


def calculate_emi(principal, annual_rate, tenure_months):
    monthly_rate = annual_rate / (12 * 100)

    if monthly_rate == 0:
        # No interest case
        emi = principal / tenure_months
    else:
        emi = (principal * monthly_rate * (1 + monthly_rate) ** tenure_months) / \
              (((1 + monthly_rate) ** tenure_months) - 1)

    total_payment = emi * tenure_months
    total_interest = total_payment - principal

    return emi, total_payment, total_interest


def get_valid_input(prompt, min_value=0):
    while True:
        try:
            value = float(input(prompt))
            if value <= min_value:
                print(f"Please enter a value greater than {min_value}.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def main():
    print("=" * 45)
    print("        LOAN EMI CALCULATOR")
    print("=" * 45)

    principal = get_valid_input("Enter Principal Amount (₹): ")
    annual_rate = get_valid_input("Enter Annual Interest Rate (%): ")
    tenure_months = int(get_valid_input("Enter Loan Tenure (months): "))

    emi, total_payment, total_interest = calculate_emi(principal, annual_rate, tenure_months)

    print("\n" + "-" * 45)
    print("RESULT")
    print("-" * 45)
    print(f"Principal Amount   : ₹ {principal:,.2f}")
    print(f"Annual Interest    : {annual_rate:.2f} %")
    print(f"Loan Tenure        : {tenure_months} months")
    print("-" * 45)
    print(f"Monthly EMI        : ₹ {emi:,.2f}")
    print(f"Total Payment      : ₹ {total_payment:,.2f}")
    print(f"Total Interest     : ₹ {total_interest:,.2f}")
    print("=" * 45)

    again = input("\nCalculate another EMI? (y/n): ").strip().lower()
    if again == 'y':
        main()
    else:
        print("Thank you for using the Loan EMI Calculator!")


if __name__ == "__main__":
    main()
