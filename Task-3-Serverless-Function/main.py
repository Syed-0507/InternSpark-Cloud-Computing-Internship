import functions_framework
from flask import jsonify

@functions_framework.http
def hello_http(request):
    return jsonify({
        "message": "Hello from InternSpark Serverless Function!",
        "status": "success",
        "platform": "Google Cloud Run",
        "language": "Python"
    })
