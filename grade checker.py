
print("--- Simple Grade Checker ---")


student_name = input("Enter student name: ").strip().title()


marks = float(input("Enter marks (0 to 100): "))

student_data = [student_name, marks]


if marks >= 40:
    status = "Passed"
    print(f"Result: {student_name} has passed!")
else:
    status = "Failed"
    print(f"Result: {student_name} has failed")

# Day 49 & 50: Saving the result into a simple text file
with open("grades.txt", "w") as file:
    file.write(f"Student: {student_data[0]}\n")
    file.write(f"Marks: {student_data[1]}\n")
    file.write(f"Status: {status}\n")

print("\nResult successfully saved to 'grades.txt'!")
