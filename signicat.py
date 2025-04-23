import http.server

# Define server address and port
host = 'localhost'
port = 8000

# Create an HTTP server instance
httpd = http.server.HTTPServer((host, port), http.server.SimpleHTTPRequestHandler)

print(f"Serving HTTP on {host}:{port}")
httpd.serve_forever()
