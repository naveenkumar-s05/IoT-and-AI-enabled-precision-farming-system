import http.server
import socketserver
import os
import socket

# ======== CONFIGURATION ========
PORT = 5500  # Change if needed
DIRECTORY = "."  # Folder to share
# ===============================

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def get_local_ip():
    """Get actual local IP address connected to the network."""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # connect() for UDP doesn't send packets
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = "127.0.0.1"
    finally:
        s.close()
    return ip

local_ip = get_local_ip()
print(f"\nYour laptop's local IP: http://{local_ip}:{PORT}")
print("Serving files from:", os.path.abspath(DIRECTORY))

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("\n🚀 Server started! Press CTRL+C to stop.")
    httpd.serve_forever()
