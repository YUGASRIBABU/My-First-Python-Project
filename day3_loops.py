# 1. create a list of different birth years
voters = [2000, 2010, 1995, 2012, 1988]

# 2. Start a loop to check every single year in that list automatically
for year in voters:
    age = 2026 - year

# 3. Check the age requirements automatically
    if age >= 18:
        print(f"Born in {year}: Age is {age}. Eligible to voat! 🗳️")
    else:
        print(f"Born in {year}: Age is {age}. Too young to vote. ❌")
