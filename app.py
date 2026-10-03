
from http.server import HTTPServer, BaseHTTPRequestHandler

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>DevOps Dashboard</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: #f4f6f8;
            color: #222;
        }

        header {
            background: #1f2937;
            color: white;
            padding: 30px;
            text-align: center;
        }

        header h1 {
            margin: 0;
            font-size: 36px;
        }

        header p {
            margin-top: 10px;
            color: #d1d5db;
        }

        .container {
            max-width: 900px;
            margin: 40px auto;
            padding: 20px;
        }

        .cards {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 20px;
        }

        .card {
            background: white;
            padding: 25px;
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        }

        .card h2 {
            margin-top: 0;
        }

        .status {
            color: #16a34a;
            font-weight: bold;
        }

        footer {
            text-align: center;
            margin-top: 40px;
            color: #6b7280;
        }
    </style>
</head>

<body>

<header>
    <h1>🚀 DevOps Dashboard</h1>
    <p>Jenkins + Docker + Python</p>
</header>

<div class="container">

    <div class="cards">

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

    </div>

    <footer>
        DevOps Practice Project · Built with Python, Docker & Jenkins
    </footer>

</div>

</body>
</html>
"""


class DevOpsHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(HTML.encode())


server = HTTPServer(("0.0.0.0", 8000), DevOpsHandler)

print("DevOps Dashboard running on port 8000")

server.serve_forever()
