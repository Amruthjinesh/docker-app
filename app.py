from http.server import HTTPServer, BaseHTTPRequestHandler

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>DevOps & Dashboard</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 50px auto;
            padding: 20px;
            background: #f5f5f5;
        }

        .card {
            background: white;
            padding: 20px;
            margin: 15px 0;
            border-radius: 10px;
        }

        h1 {
            text-align: center;
        }

        .status {
            font-weight: bold;
        }
    </style>
</head>

<body>

<h1>🚀 DevOps Dashboard</h1>
<p style="text-align:center;">Jenkins + Docker + Python</p>

<div class="card">
    <h2>🐳 Docker</h2>
    <p class="status">● Running</p>
    <p>Application is running inside a Docker container.</p>
</div>

<div class="card">
    <h2>🔧 Jenkins</h2>
    <p class="status">● Connected</p>
    <p>Jenkins builds and deploys the application.</p>
</div>

<div class="card">
    <h2>🔄 CI/CD</h2>
    <p class="status">● Automated</p>
    <p>Code is built and deployed through the pipeline.</p>
</div>

<div class="card">
    <h2>☁️ Cloud</h2>
    <p class="status">● DevOps Environment</p>
    <p>Ready for cloud deployment.</p>
</div>

<p style="text-align:center;">
    DevOps Practice Project · Built with Python, Docker & Jenkins
</p>

</body>
</html>
"""

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(HTML.encode("utf-8"))

server = HTTPServer(("0.0.0.0", 8000), Handler)

print("Server running on port 8000")

server.serve_forever()
