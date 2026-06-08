birth_year_text = input(" What is your birth year? ")

birth_year_number = int(birth_year_text)

age = 2026 - birth_year_number

print("Your age is? ")
print(age)

if age >= 18:
    print("you are an adult. You can voat! 🗳️")
else:
    print("You are a minor. No voting for you yet! 👶")
