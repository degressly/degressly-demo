from mitmproxy import http
import os

def request(flow):
    original_host = flow.request.host_header
    original_scheme = flow.request.scheme

    flow.request.host = 'degressly-downstream'
    flow.request.port = 8080
    flow.request.scheme = "http"

    # Change the Host header to the original destination
    if original_host:
        flow.request.host_header = original_host

    # Optionally, log or debug the redirected flow
    print(f"Redirecting HTTPS request to HTTP as: {flow.request.url}")

    flow.request.headers["X-Forwarded-Proto"] = original_scheme
    flow.request.headers["x-degressly-caller"] = os.getenv("PROXY_HEADER")
