# A small database of user trying to access our  system
user_names = ["alex", "sam", "BANNERD_USER", "chris", "taylor"]

# Loop through the database to grant access
for user in user_names:
    if user == "BANNERD_USER":
        print("🚨SKIPPING BANNED USER! Throwing them out of linr...")
        continue  # this skip the rest of this turn and move to the next name!

    print(f"Welcome back, {user}! Access granted. ✅")
