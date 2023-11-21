import mysql.connector
from flask import Flask, request, jsonify

# Connect to the MySQL server
mydb = mysql.connector.connect(
  host="192.168.122.199",
  user="admin",
  password="12345",
  database="mysql"
)

# Create a new table if it doesn't exist
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS numbers (number INT PRIMARY KEY)")

# Function to process the request
def process_request(number):
    # Check if the number has already been received
    mycursor.execute("SELECT * FROM numbers WHERE number = %s", (number,))
    result = mycursor.fetchone()
    if result:
        # Number has already been received, output error in response and log
        return {"error": f"Number {number} has already been received."}

    # Check if the incoming number is equal processed number minus one
    mycursor.execute("SELECT * FROM numbers WHERE number = %s", (number+1,))
    result = mycursor.fetchone()
    if result:
        # Incoming number is equal processed number minus one
        return {"error": f"Incoming number {number} is equal processed number {result[0]} minus one."}
    # Number is valid, increase it by one and send it back in the response
    mycursor.execute("INSERT INTO numbers (number) VALUES (%s)", (number,))
    new_number = number + 1
    mydb.commit()
    return {"number": new_number}

# Start the web server
app = Flask(__name__)

@app.route("/", methods=["POST"])
def handle_request():
    number = request.json["number"]
    result = process_request(number)
    return jsonify(result)

if __name__ == "__main__":
    app.run(port=5000)
