import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Define user profile
class UserProfile:
    def __init__(self, name, age, income, savings, expenses, risk_tolerance, goals):
        self.name = name
        self.age = age
        self.income = income
        self.savings = savings
        self.expenses = expenses
        self.risk_tolerance = risk_tolerance  # 'low', 'medium', 'high'
        self.goals = goals  # e.g. {'retirement': 65, 'buy_home': 5}

    def net_savings(self):
        return self.income - self.expenses

    def summary(self):
        return {
            "Name": self.name,
            "Age": self.age,
            "Monthly Income": self.income,
            "Monthly Expenses": self.expenses,
            "Current Savings": self.savings,
            "Risk Tolerance": self.risk_tolerance,
            "Financial Goals": self.goals,
        }

# Basic financial advisor logic
class InvestmentAdvisor:
    def __init__(self, user_profile: UserProfile):
        self.user = user_profile

    def recommend_investment_allocation(self):
        risk = self.user.risk_tolerance
        if risk == 'low':
            return {"Bonds": 70, "Stocks": 20, "Cash": 10}
        elif risk == 'medium':
            return {"Bonds": 40, "Stocks": 50, "Cash": 10}
        else:  # high
            return {"Bonds": 20, "Stocks": 70, "Crypto/ETFs": 10}

    def future_value(self, years=10, rate=0.05):
        """
        Estimate future value of savings with compound interest.
        """
        fv = self.user.savings * ((1 + rate) ** years)
        return round(fv, 2)

    def personalized_plan(self):
        allocation = self.recommend_investment_allocation()
        future_savings = self.future_value()
        return {
            "Recommended Allocation": allocation,
            "Estimated Future Value (10 yrs)": f"${future_savings:,}",
            "Monthly Net Savings": self.user.net_savings()
        }

# Example usage
if __name__ == "__main__":
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    income = int(input("Enter your income: "))
    savings = int(input("Enter your savings: "))
    expenses = int(input("Enter your expenses: "))
    risk_tolerance = input("Enter your risk_tolerance medium: ")
    retirement_age = int(input("Enter your retirement_age: "))
    home = int(input("Enter no. of homes to buy: "))
    
    user = UserProfile(
        name=name,
        age=age,
        income=income,
        savings=savings,
        expenses=expenses,
        risk_tolerance=risk_tolerance,
        goals={'retirement': retirement_age, 'buy_home': home}
    )

    advisor = InvestmentAdvisor(user)

    print("=== USER PROFILE ===")
    for k, v in user.summary().items():
        print(f"{k}: {v}")

    print("\n=== PERSONALIZED PLAN ===")
    plan = advisor.personalized_plan()
    for k, v in plan.items():
        print(f"{k}: {v}")
