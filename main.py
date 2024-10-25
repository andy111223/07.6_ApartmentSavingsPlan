import numpy as np
import numpy_financial as npf
import matplotlib.pyplot as plt

def calculate_savings_to_meet_goal(current_price, growth_rate, years, annual_rate):
    """
    Assumptions for financial calculations:
    - An asset is increasing at a given rate for a number of years.
    - You deposit an equal amount of money every month.
    - Your deposit is capitalized every month.
    - 
    
    'current_price' is the present value of an asset you are saving for.
    'growth_rate' is the compounded yearly increase rate of your asset price expressed in decimal format.
    'years' is the number of years during which your asset price will be increasing by the growth_rate.
    'annual_rate' is the rate at which your bank deposit is increased.
    """
    # Estimate future price
    future_price = -npf.fv(growth_rate, years, 0, current_price)
    print("Future price:", f"{future_price:,.2f}")

    # Calculate monthly deposit
    months = years * 12
    monthly_rate = annual_rate / 12
    savings_goal = future_price

    monthly_deposit = npf.pmt(monthly_rate, months, 0, -savings_goal)
    print("Monthly deposit needed:", f"{monthly_deposit:,.2f}")

    # Initialize arrays to track each month's balance
    savings_balance = np.zeros(months)  
    current_balance = 0 

    # Calculate the cumulative savings balance month-by-month
    for i in range(months):
        current_balance = current_balance * (1 + monthly_rate)  
        current_balance += monthly_deposit  
        savings_balance[i] = current_balance  

    # Data visualization
    price = np.around(np.linspace(current_price, future_price, months), 2)
    plt.plot(price, label='Price')
    plt.plot(savings_balance, label='Savings Balance')
    plt.legend()
    plt.xlabel('Months')
    plt.ylabel('Money')
    plt.title('Savings Growth vs. Price')
    plt.show()

    return savings_balance, future_price

# Example usage
calculate_savings_to_meet_goal(current_price=120000, growth_rate=0.05, years=5, annual_rate=0.12)


