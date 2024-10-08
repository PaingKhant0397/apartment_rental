from livereload import Server
import subprocess
import os

def start_server():
    # Start the server in a subprocess
    return subprocess.Popen(['python3', 'index.py'], preexec_fn=os.setsid)

if __name__ == '__main__':
    server = Server()
    server.watch('*.py', start_server)  # Watch for changes in any .py file
    server.serve(port=8000, root='.')
