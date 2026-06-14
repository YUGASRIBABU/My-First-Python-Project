# Day 8:The Automated Ages of People in Loop
age_people = [12, 45, 66, 89]
index = 0

# The loop runs as long as our index is valid
while index < len(age_people):
    current_age = age_people[index]
    print(f"Round {index + 1} | Processing Age: {current_age}")

    # Check if the score is even or odd using modulo operator (%)
    if current_age % 2 == 0:
        final_age = current_age * 2  # Even
        print(
            f"-> Even Number Detected! multiplying age by 2. Final:{final_age}")
    else:
        final_age = current_age + 5  # Odd
        print(f"-> Odd Number Detected! Adding 5 to age. Final:{final_age}")

    # increment the index to the next people
    index += 1
    print("-" * 40)
