# rupee_text_to_number.py
amount = "Rs 1,250.50"

amount = amount.replace("Rs", "").replace(",", '')
print(float(amount))
