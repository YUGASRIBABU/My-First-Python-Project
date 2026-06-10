cargo_belt = ["box_1", "damaged_box", "box_2", "BOMB", "box_3"]

print("🏭 Cargo scanning system INITALIZED...\n")

for item in cargo_belt:
    if item == "damaged_box":
        print(f"🗑️ ALERT: {item} is broken! Skipping.")
        continue

    if item == "BOMB":
        print(f"🚨 DANGER! {item} DELECTED! SHUTTING DOWN!")
        break

    print(f"📦 Cargo iteam '{item}' verified. Loading! ✅")
