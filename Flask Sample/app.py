from flask import Flask, request, render_template, jsonify
import csv
import os

app = Flask(__name__)

# Set the path to the CSV file
CSV_FILE = os.path.join(os.path.dirname(__file__), 'data.csv')

@app.route('/')
def index():
    # Read data from CSV file
    data = read_csv_data()
    return render_template('index.html', data=data)

@app.route('/submit', methods=['POST'])
def submit():
    data1 = request.form.get('data1')
    data2 = request.form.get('data2')
    data3 = request.form.get('data3')

    # Append the data to the CSV file
    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([data1, data2, data3])

    # After adding the new row, re-read all data to send back as JSON
    data = read_csv_data()
    return jsonify({
        "message": "Data added successfully",
        "data": data
    })

def read_csv_data():
    # Read the CSV file and return its content
    if not os.path.exists(CSV_FILE):
        return []

    with open(CSV_FILE, mode='r') as file:
        reader = csv.reader(file)
        next(reader, None)  # Skip header if present
        return [row for row in reader]

import socketserver

with socketserver.TCPServer(("localhost", 0), None) as s:
    free_port = s.server_address[1]
    if __name__ == '__main__':   #Ensures this block runs only if app.py is executed directly (not imported as a module).
    #app.run(debug=True, port= free_port)#Starts the Flask development server, with debug=True to allow auto-reloading and provide error messages during development.
    # This also picks a random available port each time it runs. This ensures that flask will run
        app.run(host = "0.0.0.0", port=free_port)
