#!/usr/bin/env python3
#
# Exempel för DSD400-kursen. Webbserver som tillhandahåller statiska
# filer från "html"-katalogen samt genererad dynamiskt JSON för
# URL:er som börjar på "/api".


from http.server import SimpleHTTPRequestHandler, HTTPServer
import json, random, datetime
import pymysql.cursors

connection = pymysql.connect(host='dsd400.port0.org',
                             user='pySOEL',
                             password='Rotmos3718'.encode().decode('latin1'),
                             database='ElheSobe13',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
INTERFACES = 'localhost'
PORT = 8020

# This class will handle any incoming GET requests
# URLs starting with /api/ is catched for REST/JSON calls
# Other URLs are handled by default handler to serve static
# content (directories, files)

class RequestHandler(SimpleHTTPRequestHandler):
    
    def do_GET(self):
        print("Requested path:", self.path)  # Debugging print
        if self.path.startswith('/api/book'):
            self.send_response(200)
            self.send_header('Content-type', 'text/json')
            self.end_headers()

            
            with connection.cursor() as cursor:
                cursor.execute("SELECT BookingID, StudentID, RoomID  FROM Booking")
                response = cursor.fetchall()
                for i in response:
                    print(i)
                

            # Send the JSON response
            self.wfile.write(json.dumps(response).encode())
            return
        else:
            # Handle non-API requests
            self.path = '/html' + self.path if not self.path.startswith('/html') else self.path
            super().do_GET()

try:
    server = HTTPServer((INTERFACES, PORT), RequestHandler)
    print('Starting HTTP server on http://' + INTERFACES + ":" + str(PORT))
    server.serve_forever()
except KeyboardInterrupt:
    print('Ctrl-C received, shutting down the web server')
    server.socket.close()


