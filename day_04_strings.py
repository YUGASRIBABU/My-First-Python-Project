my_name = "Yugasri Babu"
name_length = len(my_name)

print(f"My name is {my_name} and it has {name_length} letters!")

# 1. force the whole name to UPPERCASE
print(my_name.upper())

# 2. Swap out "Babu" for "The Developer"
hero_name = my_name.replace("Babu", "The Developer")
print(hero_name)

# 3. Clean up accidental space automatically
dirty_input = "  Microsof AI Fest 2026  "
print(dirty_input.strip())
