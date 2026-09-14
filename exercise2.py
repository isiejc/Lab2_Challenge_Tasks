print("Signal Diagnnostic System")

surname = "CRUZ"
SEED_NUM = 8

print("Surname:", surname)
print("Seed Number:", SEED_NUM)

signal = surname + str(SEED_NUM) + "!@#"

print("Generated Signal:", signal)

print("\n=== CHARACTER ANALYSIS ===")

letters = 0
numbers = 0
spaces = 0
special = 0

log = []

for char in signal:
    print("Character:", char)

    if char.isalpha():
        print("Type: LETTERS")
        letters += 1
        log.append("Character " + char + ": LETTER" )

    elif char.isdigit():
        print("Type: NUMBERS")
        numbers += 1
        log.append("Character " + char + ": NUMBER" )

    elif char.isspace():
        print("Type: SPACES")
        spaces += 1
        log.append("Character " + char + ": SPACE" )

    else:
        print("Type: SPECIAL CHARACTER")
        special += 1
        log.append("Character " + char + ": SPECIAL CHARACTER" )

print("\n=== DIAGNOSTIC SUMMARY ===")

print("Total Letters:", letters)
print("Total Numbers:", numbers)
print("Total Spaces:", spaces)
print("Total Special Characters:", special)

print("\n=== EXECUTION LOG ===")

for entry in log:
    print(entry)

print("\n=== END OF DIAGNOSTIC ===")
print("Signal:", signal)
print("Total Characters:", len(signal))

print("\nSignal analysis completed. Thank you for using the Signal Diagnostic System.")