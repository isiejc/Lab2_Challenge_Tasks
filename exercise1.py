import random
print("Sensor Monitoring System")

surname = "CRUZ"
SEED_NUM = 8

print("Surname:", surname)
print("Seed Number:", SEED_NUM)

random.seed(surname + str(SEED_NUM))

valid = 0
invalid = 0

normal = 0
warning = 0
critical = 0

log = []
generated_data = []
results = []
classifications = []

for i in range(1, 6):
    reading = random.randint(-20, 120)
    generated_data.append(reading)

    log.append("Reading " + str(i) + " generated: " + str(reading))
    
    print("\nSensor Reading:", i, ":", reading)

    if reading >= 0 and reading <= 100:
        print("Status: VALID")
        valid += 1
        results.append("Reading " + str(i) + ": VALID")

        if reading <= 50:
            print("Classification: NORMAL")
            normal += 1
            classifications.append("Reading " + str(i) + ": VALID - NORMAL")
            log.append("Reading " + str(i) + ": VALID - NORMAL")
        elif reading <= 80:
            print("Classification: WARNING")
            warning += 1
            classifications.append("Reading " + str(i) + ": VALID - WARNING")
            log.append("Reading " + str(i) + ": VALID - WARNING")
        else:
            print("Classification: CRITICAL")
            critical += 1
            classifications.append("Reading " + str(i) + ": VALID - CRITICAL")
            log.append("Reading " + str(i) + ": VALID - CRITICAL")

    else:
        print("Status: INVALID")
        invalid += 1
        readings.append("Reading " + str(i) + ": INVALID")
        log.append("Reading " + str(i) + ": INVALID")     

print("\n=== GENERATED SENSOR DATA ===")

for reading in generated_data:
    print(reading)

print("\n=== READING RESULTS ===")

for result in results:
    print(result)

print("\n=== CLASSIFICATION RESULTS ===")    

for classification in classifications:
    print(classification)

print("\n=== FINAL SUMMARY ===")
print("Valid Readings:", valid)
print("Invalid Readings:", invalid)
print("Normal:", normal)
print("Warning:", warning)
print("Critical:", critical)              

print("\n=== EXECUTION LOG ===")

for entry in log:
    print(entry)

print("\nProgram completed successfully.")