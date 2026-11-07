# average_skipping_blanks.py

v = {120, None, 80}
x = {a for a in v if a is not None}
print(sum(x) / len(x))
