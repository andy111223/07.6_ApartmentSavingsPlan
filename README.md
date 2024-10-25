# Apartment Savings Plan Calculator

The Apartment Savings Plan Calculator helps users estimate monthly savings required to afford a future apartment purchase. It takes into account increasing property prices and compounding interest from monthly savings deposits.

## Features
- **Future Price Estimation**: Calculates the projected price of an asset (e.g., an apartment) over time given an annual growth rate.
- **Savings Plan Calculation**: Determines the required monthly deposit to meet the target amount for a future purchase.
- **Graphical Comparison**: Visualizes the growth of savings versus the future price of the asset over a given number of months.

## Installation
1. Clone this repository to your local machine:  
   ```git clone https://github.com/andy111223/07.6_ApartmentSavingsPlan.git```
2. Navigate to the project directory:  
   ```cd 07.6_ApartmentSavingsPlan```
3. Install the required dependencies (if not already installed):  
   ```pip install numpy numpy-financial matplotlib```
4. Run the script:  
   ```python3 main.py```

## Usage
The script calculates the estimated monthly deposit required to save for an asset like an apartment over a specified number of years, taking into account:
- Asset price growth rate (e.g., 5% per year).
- Monthly deposits earning interest at a specified annual rate (e.g., 12%).

It then displays a graph showing:
- The growth of the asset price over time.
- The accumulation of savings over time.

Users can modify the parameters such as the initial asset price, growth rate, number of years, and annual rate to see different outcomes.

## Requirements
- Python 3 (tested on Python 3.12)
- NumPy library
- NumPy-financial library
- Matplotlib library