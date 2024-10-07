from mitmproxy import http

def request(flow: http.HTTPFlow) -> None:
    original_host = flow.request.host_header


    flow.request.host = 'degressly-downstream'
    flow.request.port = 8080
    flow.request.scheme = "http"

    # Change the Host header to the original destination
    if original_host:
        flow.request.host_header = original_host

    # Optionally, log or debug the redirected flow
    print(f"Redirecting HTTPS request to HTTP: {flow.request.url}")

    flow.request.headers["X-Forwarded-Proto"] = "https"
