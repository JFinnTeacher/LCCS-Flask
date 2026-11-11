import socketserver

with socketserver.TCPServer(("localhost", 0), None) as s:
    free_port = s.server_address[1]
    if __name__ == '__main__':   #Ensures this block runs only if app.py is executed directly (not imported as a module).
    #app.run(debug=True, port= free_port)#Starts the Flask development server, with debug=True to allow auto-reloading and provide error messages during development.
        app.run(host = "0.0.0.0", port=free_port)