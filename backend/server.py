
from http.server import HTTPServer
import signal
import sys
from utils import setup_logger
from app import RequestHandler

logger = setup_logger(__name__)


def run(server_class=HTTPServer, handler_class=RequestHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)

    def handle_exit(signum, frame):
        print("Shutting down server...")
        httpd.server_close()
        sys.exit(0)

    signal.signal(signal.SIGINT, handle_exit)  # Handle Ctrl+C
    signal.signal(signal.SIGTERM, handle_exit)  # Handle termination

    logger.info(f'Starting http on port {port}')
    httpd.serve_forever()
