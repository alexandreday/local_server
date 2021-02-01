import http.server
import socketserver
import sys
import os
import random
import string
import time
import platform
import shutil
import threading
import subprocess

def random_string(n=50):
    return ''.join(random.choice(string.ascii_lowercase + string.digits)
                   for _ in range(n))

def open_file(filename):
    if platform.system() == 'Darwin':       # macOS
        subprocess.call(('open', filename))
    elif platform.system() == 'Windows':    # Windows
        os.startfile(filename)
    else:                                   # linux variants
        subprocess.call(('xdg-open', filename))

def run_cp_kill(html_page):
    # Run local server
    tmp_file = html_page.strip('.html') + '_' + random_string() + '.html'
    shutil.copyfile(html_page, tmp_file)
    # Run python server on a different thread
    threading.Thread(target=run_local_server, daemon=True).start()
    time.sleep(0.5) # wait for server to launch
    url = 'http://localhost:8499/%s' % tmp_file
    open_file(url)
    time.sleep(0.5)
    os.remove(tmp_file)

def run_local_server(port = 8000):
    # https://stackoverflow.com/questions/15260558/python-tcpserver-address-already-in-use-but-i-close-the-server-and-i-use-allow
    socketserver.TCPServer.allow_reuse_address = True # required for fast reuse ! 
    Handler = http.server.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer(('', port), Handler)
    print('Creating server at port', port)
    httpd.serve_forever()

if __name__ == '__main__':
    html_page = 'index.html'
    if len(sys.argv) == 2:
        html_page = str(sys.argv[1])
    print(html_page)
    run_cp_kill(html_page)
