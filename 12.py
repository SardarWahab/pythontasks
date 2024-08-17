# Define a dictionary with student names as keys and their scores as values
student_scores = {
    'Alice': 88,
    'Bob': 72,
    'Charlie': 95,
    'Diana': 64,
    'Eva': 79
}

# Define the grade boundaries
grade_boundaries = {
    'A': 90,
    'B': 80,
    'C': 70,
    'D': 60,
    'F': 0
}

# Initialize variables to calculate the total score
total_score = 0
num_students = len(student_scores)

# Loop through each student and their score
for student, score in student_scores.items():
    # Determine the grade for the current score
    grade = 'F'  # Default grade
    for grade_letter, boundary in grade_boundaries.items():
        if score >= boundary:
            grade = grade_letter
            break
    
    # Print the student's name, score, and grade
    print(f'{student} scored {score}, which is a grade of {grade}.')
    
    # Add the score to the total score
    total_score += score

# Calculate the average score
average_score = total_score / num_students

# Print the average score
print(f'\nThe average score of the students is {average_score:.2f}.')
print
