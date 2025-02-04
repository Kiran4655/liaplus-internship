from flask import Flask, render_template_string
from datetime import datetime
import os

application = Flask(__name__)

# HTML template
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>AWS Python App</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 40px;
            text-align: center;
            background-color: #f5f5f5;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background-color: white;
            border: 1px solid #ddd;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .info {
            margin-top: 20px;
            padding: 10px;
            background-color: #f8f9fa;
            border-radius: 4px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Hello from AWS Python!</h1>
        <p>This Flask application is running on AWS Elastic Beanstalk</p>
        <div class="info">
            <p>Server Time: {{ server_time }}</p>
            <p>Environment: {{ environment }}</p>
        </div>
    </div>
</body>
</html>
'''

@application.route('/')
def home():
    return render_template_string(
        HTML_TEMPLATE,
        server_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        environment=os.environ.get('FLASK_ENV', 'production')
    )

if __name__ == '__main__':
    application.run(host='0.0.0.0', port=8000)
