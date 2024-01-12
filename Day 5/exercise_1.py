# student_heights = [180, 124, 165, 173, 189, 169, 146]
student_heights = input("Input a list of student heights ").split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

total_students = 0
sum_of_heights = 0
for height in student_heights:
    total_students += 1
    sum_of_heights += height

average = round(sum_of_heights / total_students)

print(f"Average height is {average}")

# # Easy Solution
# total_height = sum(student_heights)
# number_of_students = len(student_heights)
# average_height = round(total_height / number_of_students)
# print(average_height)
