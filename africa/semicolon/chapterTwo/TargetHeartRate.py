age = int(input("Enter your age: "))


def maximum_heart_rate():
    mhr = 220 - age
    return mhr


def target_heart_rate():
    minimumTargetHeartRate = 0.5 * (maximum_heart_rate())
    maximumTargetHeartRate = 0.85 * (maximum_heart_rate())
    print("Your target heart rate is: ", minimumTargetHeartRate, " - ", maximumTargetHeartRate, "BPM")


print("Your maximum heart rate is: ", maximum_heart_rate(), "BPM")
print(target_heart_rate())

