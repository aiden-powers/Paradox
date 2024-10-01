import json
import threading
import tkinter as tk
from http.server import HTTPServer, BaseHTTPRequestHandler

HOST = '127.0.0.1'
PORT = 3000

shared_data = {}

class RequestHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        global shared_data
        content_length = int(self.headers.get('Content-Length', 0))
        data = json.loads(self.rfile.read(content_length).decode('utf-8'))
        shared_data = data
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        self.wfile.write(b'')

    def do_GET(self):
        print("Unexpected GET request received")
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        html = f"<html><body>HTTP Server running at http://{HOST}:{PORT}</body></html>"
        self.wfile.write(html.encode('utf-8'))

    def log_message(self, format, *args):
        return

def update_label1(label):
    if "phase_countdowns" in shared_data:
        label.config(text=f"{round(float(shared_data["phase_countdowns"]["phase_ends_in"]))}")
    else: label.config(text="No data")
    label.after(100, update_label1, label)

def update_label2(label):
    if "phase_countdowns" in shared_data:
        label.config(text=f"{shared_data["phase_countdowns"]["phase"]}")
    else: label.config(text="No data")
    label.after(100, update_label2, label)

def create_tkinter_window():
    """Function to create a tkinter window with a label."""
    root = tk.Tk()
    root.title("Data Viewer")
    root.geometry("256x128")
    root.configure(background='black')
    label1 = tk.Label(root, text="No data available", font=("Helvetica", 24), bg="black",fg="white", justify="center")
    label1.pack(padx=5, pady=5)
    label2 = tk.Label(root, text="No data available", font=("Helvetica", 24), bg="black",fg="white", justify="center")
    label2.pack(padx=5, pady=5)
    update_label1(label1)
    update_label2(label2)
    root.mainloop()

def run_server():
    server_address = (HOST, PORT)
    httpd = HTTPServer(server_address, RequestHandler)
    print(f"Server running at http://{HOST}:{PORT}")
    httpd.serve_forever()

if __name__ == '__main__':
    server_thread = threading.Thread(target=run_server)
    server_thread.daemon = True
    server_thread.start()
    create_tkinter_window()
