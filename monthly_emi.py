# monthly_emi.py
principle, rate, interest = 500000, 0.09 / 12, 60
fraction = (1 + rate) ** interest

print(round(principle * rate * fraction / (fraction - 1)))
