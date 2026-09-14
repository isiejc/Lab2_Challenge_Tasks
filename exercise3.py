print("Electronic Access System")

surname = "CRUZ"
SEED_NUM = 8

print("Surname:", surname)
print("Seed Number:", SEED_NUM)

attempt_limit = 3

print("Attempt Limit:", attempt_limit)

password = surname.lower() + str(SEED_NUM)

print("Generated Password:", password)

normalized_password = password.strip().lower()

print("Normalized Password:", normalized_password)

print("\n=== PASSWORD ANALYSIS ===")

for char in normalized_password:
    print("Character:", char)

attempts = 0
access_granted = False
log = []

print("\n=== AUTHENTICATION ===")

while attempts < attempt_limit:
    entered_password = input("Enter password: ")
    attempts += 1

    if entered_password.strip().lower() == normalized_password:
        print("Access Granted!")
        access_granted = True
        log.append("Attempt " + str(attempts) + ": ACCESS GRANTED")
        break

    else:
        print("Access Denied.")
        log.append("Attempt " + str(attempts) + ": ACCESS DENIED")

print("\n=== FINAL SYSTEM STATE ===")

if access_granted:
    final_state = "UNLOCKED"
    access_result = "ACCESS GRANTED"
else:
    final_state = "LOCKED"
    access_result = "ACCESS DENIED"

print("Access Result:", access_result)
print("Final System State:", final_state)
      
print("\n=== ASSESSMENT DATA ===")

print("Attempts Made:", attempts)
print("Access Result:", access_result)
print("Final System State:", final_state)

print("\n=== EXECUTION LOG ===")

for entry in log:
    print(entry)

print("\n=== FINAL OUTPUT ===")

print("Generated Password:", password)
print("Attempts Limit:", attempt_limit)
print("Attempts Made:", attempts)
print("Access Result:", access_result)
print("Final System State:", final_state)

print("\nAuthentication process completed.")