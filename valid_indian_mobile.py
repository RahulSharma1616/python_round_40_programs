# valid_indian_mobile.py
import re

mobile_number = '9876543210'
print(bool(re.fullmatch(r"[6-9]\d{9}", mobile_number)))
