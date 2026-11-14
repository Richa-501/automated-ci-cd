from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

APP_VERSION = "1.0.0"

@app.route("/")
def home():
    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>My Flask Application</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f0f4f8;
                text-align: center;
                padding: 100px 20px;
            }

            .container {
                background: white;
                padding: 40px;
                border-radius: 10px;
                max-width: 600px;
                margin: auto;
            }

            h1 {
                color: #2563eb;
            }

            p {
                color: #555;
                font-size: 18px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Welcome to My Flask Application!</h1>
            <p>Built using Python Flask.</p>
            <p>Automated with Docker and GitHub Actions.</p>
            <p>Application Version: {{ version }}</p>
        </div>
    </body>
    </html>
    """, version=APP_VERSION)


@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200


@app.route("/version")
def version():
    return jsonify({"version": APP_VERSION}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
