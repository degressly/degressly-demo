from flask import Flask, Response
import sys
import requests
import json

port = sys.argv[1]

app = Flask(__name__)

@app.route("/")
def hello_world():
    url = "https://api.ipify.org?format=json"

    payload = {"test": port, "constant": "constant", "will_regress": "no_regress"}

    if (port == '8082'):
        payload["will_regress"] = "This field should be different to prove a point."


    headers = {"Content-Type": "application/json"}
    print(payload)
    requests.request("GET", url, headers=headers, data=payload)
    
    return Response(json.dumps(payload), content_type="application/json")



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port)