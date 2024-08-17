# Step 1: Create a dictionary of employees
employees = {
    "John": [3.5, 4.0, 3.7],
    "Jane": [4.2, 4.5, 4.0],
    "Doe": [2.8, 3.0, 2.9],
}

# Step 2: Add new ratings
new_ratings = {
    "John": 4.2,
    "Jane": 4.8,
    "Doe": 3.1,
}

for name, rating in new_ratings.items():
    if name in employees:
        employees[name].append(rating)

# Step 3: Calculate and print average rating
for name, ratings in employees.items():
    average_rating = sum(ratings) / len(ratings)
    # Step 4: Determine performance status
    if average_rating < 3.0:
        status = "Needs Improvement"
    elif average_rating >= 4.0:
        status = "Excellent"
    else:
        status = "Satisfactory"
    
    # Step 5: Print employee performance status
    print(f"Employee: {name}, Average Rating: {average_rating:.2f}, Performance Status: {status}")
