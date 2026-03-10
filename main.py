from flask import Flask,request,jsonify,json
import os
import io
import sys

app = Flask(__name__)

@app.route("/")
def home():
    return "working"

@app.route("/execute",methods=['POST'])
def run_code():
    code = request.json["code"]
    global captured_output
    try:
        output = io.StringIO()
        sys.stdout = output
        exec(code)
        sys.stdout = sys.__stdout__
        captured_output = output.getvalue()
        output.close()
        status = "compilation succesfull"
        # print("success",status)
    except Exception as e:
        status = "compilation failed!"
        captured_output = str(e)
        
    return jsonify({
        "status" : status,
        "output": captured_output
    })

port = int(os.environ.get("PORT", 8000))  # Render provides PORT
app.run(host="0.0.0.0", port=port)