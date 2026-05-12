import csv

male_age_sum = 0
male_count = 0

female_dead = {"1": 0, "2": 0, "3": 0}

with open("Big Data Analytics\\Titanic\\titanic.csv", "r") as file:

    data = csv.DictReader(file)

    for row in data:

        if row["Sex"] == "male" and row["Survived"] == "0":
            male_age_sum += int(row["Age"])
            male_count += 1

        if row["Sex"] == "female" and row["Survived"] == "0":
            female_dead[row["Class"]] += 1


print("Average age of dead males:",
      male_age_sum / male_count)

print("\nFemale deaths by class:")

for cls, count in female_dead.items():
    print("Class", cls, ":", count)