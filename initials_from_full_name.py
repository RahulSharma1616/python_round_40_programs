# initials_from_full_name.py

name = 'Rahul Sharma'
initials = ''.join(word[0] for word in name.split())

print(initials)
