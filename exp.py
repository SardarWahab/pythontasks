# a = input("Enter the number")
# print(f"multiplication of table {a} is ")
# try:
#     for i in range(1,11):
#         print(f"{int(a)} x {i}= {int(a)*i}")
# except :
#    print("Invalid input")
# print("Some impoortant line of code")   
# print("End of program")
from flask import Flask

# Create a Flask app instance
app = Flask(__name__)

# Define a route and its corresponding function
@app.route('/')
def hello_world():
    return 'Hello, World!'

# Run the app if this script is executed directly
if __name__ == '__main__':
    app.run()
