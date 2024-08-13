# students = {
#     "student1": {"name": "Alice", "age": 20, "grades": [85, 90, 92]},
#     "student2": {"name": "Bob", "age": 22, "grades": [78, 81, 85]},
#     "student3": {"name": "Charlie", "age": 19, "grades": [95, 89, 94]},
# }
# print(students["student2"]["grades"])



                                 # 2nd 
# subjects = {
#     "Math": ["Alice", "Bob"],
#     "Science": ["Alice", "Charlie"],
#     "History": ["Bob", "Charlie"],
# }
# if "David" not in subjects["Math"]:
#     subjects["Math"].append("David")
    
# print(subjects)


                        #  3rd
# employees = {"John": 50000, "Jane": 60000, "Doe": 45000}
# raise_threshold = 50000
# raise_amount = 5000

# for employee, salary in employees.items():
#     if salary < raise_threshold:
#         employees[employee] += raise_amount

# print(employees)
   
                            # 4th


# dict1 = {"a": 1, "b": 2, "c": 3}
# dict2 = {"b": 4, "c": 5, "d": 6}

# common_keys = dict1.keys() & dict2.keys()
# print(common_keys)


#                       5th
# data = {"name": "Alice", "age": 25, "city": "New York"}
# data.pop("city")
# print(data)




#                                 6th

# data1 = {"name": "Alice", "age": 25}
# data2 = {"city": "New York", "country": "USA"}
# merged_data = {**data1, **data2}
# print(merged_data)



                                #   7th


# data = {"name": "Alice", "age": 25}
# exists = "age" in data
# print(exists)



                                    #7th


# keys = ["name", "age", "city"]
# default_value = "Unknown"
# data = dict.fromkeys(keys, default_value)
# print(data)

                                              # 8th


# pairs = [("name", "Alice"), ("age", 25), ("city", "New York")]
# data = dict(pairs)
# print(data)



# 9th


# data = {"a": 10, "b": 25, "c": 5}
# max_key = max(data, key=data.get)
# print(max_key)


# 10th

# tuples_list = [("a", 1), ("b", 2), ("c", 3)]
# data = dict(tuples_list)
# print(data)
