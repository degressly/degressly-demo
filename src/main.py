from flask import Flask, Response, request
import sys, requests, json, time

port = sys.argv[1]

app = Flask(__name__)

@app.route("/<route>")
def hello_world(route):
    url = "https://postman-echo.com"

    payload = {"test": port, "constant": "constant", "will_regress": "no_regress", "time": time.time(), "price": 99.95}

    if (port == '8082'):
        url = "https://google.com"
        payload["will_regress"] = "This field should be different to prove a point."
        payload["price"] = "99.94"

    print(request.headers)

    headers = {
        "content-type": "application/json",
        "x-degressly-trace-id": request.headers.get("x-degressly-trace-id")
    }

    print(url, headers, payload)
    resp = requests.request("POST", url, headers=headers, data=json.dumps(payload))
    print(resp)
    
    return Response(getXml(payload["price"]), content_type="application/xml")


def getXml(val):
    # Candidate will respond with 99.94 for price 
    # Primary and secondary will respond with 99.95
    return f"""<?xml version="1.0" encoding="UTF-8" ?>
 <root>
     <book category="web" cover="paperback">
         <title lang="en">Learning XML</title>
         <author>Erik T. Ray</author>
         <year>2003</year>
         <price>{val}</price>
     </book>
 </root>
"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port)