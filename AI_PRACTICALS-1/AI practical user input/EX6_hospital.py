# Simple Hospital Expert System

"""
Time Complexity:
O(1)

Because only fixed conditions are checked.

Space Complexity:
O(1)

Only small fixed memory is used.
"""

print("===================================")
print("   HOSPITAL EXPERT SYSTEM")
print("===================================\n")

# Patient Details
name = input("Enter Patient Name: ")
age = int(input("Enter Age: "))

print("\nSelect Symptoms (yes/no)\n")

fever = input("Do you have Fever? ").lower()
cough = input("Do you have Cough? ").lower()
cold = input("Do you have Cold? ").lower()
headache = input("Do you have Headache? ").lower()
stomach_pain = input("Do you have Stomach Pain? ").lower()
vomiting = input("Do you have Vomiting? ").lower()
chest_pain = input("Do you have Chest Pain? ").lower()
breathing_problem = input("Do you have Breathing Problem? ").lower()

print("\n===================================")
print("        MEDICAL REPORT")
print("===================================")

print(f"\nPatient Name : {name}")
print(f"Age          : {age}")

# Diagnosis Rules
print("\nPossible Disease and Suggestion:\n")

# Flu Check
if fever == "yes" and cough == "yes" and cold == "yes":

    print("Possible Disease : Flu / Viral Infection")
    print("Suggestion       : Drink fluids and take proper rest.")
    print("Doctor           : General Physician")

# Migraine Check
elif headache == "yes" and fever == "no":

    print("Possible Disease : Migraine")
    print("Suggestion       : Avoid stress and take proper sleep.")
    print("Doctor           : Neurologist")

# Food Poisoning Check
elif stomach_pain == "yes" and vomiting == "yes":

    print("Possible Disease : Food Poisoning")
    print("Suggestion       : Drink ORS and avoid oily food.")
    print("Doctor           : Gastroenterologist")

# Heart Problem Check
elif chest_pain == "yes" and breathing_problem == "yes":

    print("Possible Disease : Heart Disease")
    print("Suggestion       : Immediate medical attention required.")
    print("Doctor           : Cardiologist")

# Fever Only
elif fever == "yes":

    print("Possible Disease : Common Fever")
    print("Suggestion       : Take rest and stay hydrated.")
    print("Doctor           : General Physician")

# No Major Symptoms
else:

    print("No major disease detected.")
    print("Suggestion : Please consult a doctor for proper diagnosis.")

print("\n===================================")
print("     THANK YOU! GET WELL SOON")
print("===================================")