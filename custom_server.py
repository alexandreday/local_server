# Run python server on a different thread
import http.server
import socketserver
import sys, os, random, string, signal, subprocess
import time, random, string

# run a subprocess to create server
def random_string(n=50):
    return ''.join(random.choice(string.ascii_lowercase+string.digits) for _ in range(n))

def main():
    n_arg = len(sys.argv)
    if n_arg == 1:
        html_page = "index.html"
    elif n_arg == 2:
        html_page = str(sys.argv[1])
    else:
        run_local_server() # forever loop

    # Run local server
    random_tag = random_string()
    tmp_file = html_page.strip(".html") +"_"+ random_tag + ".html"
    os.system('cp %s %s'%(html_page,tmp_file))

    # Runs other process in the background
    p = subprocess.Popen('python custom_server.py run server please'.split(" "))

    time.sleep(0.5) # wait for server to launch
    url = "http://localhost:8000/%s"%tmp_file
    os.system('open %s'%url)
    time.sleep(0.5)
    os.system('rm %s'%tmp_file)

    # Now kill serverls
    kill_local_server(p.pid)

def run_local_server(port = 8000):
    socketserver.TCPServer.allow_reuse_address = True # required for fast reuse ! 
    """
    Check out :
    https://stackoverflow.com/questions/15260558/python-tcpserver-address-already-in-use-but-i-close-the-server-and-i-use-allow
    """
    Handler = http.server.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer(("", port), Handler)
    print("Creating server at port", port)
    httpd.serve_forever()

def kill_local_server(pid):
    test = os.kill(pid, signal.SIGTERM) # kills subprocess, allowing clean up

if __name__ == "__main__":
    main()