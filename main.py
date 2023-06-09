import argparse

from config import HOST, PORT, DEBUG
from server import run_server
from serverless import run_serverless

parser = argparse.ArgumentParser(description="Finds file duplicates using hash.",
                                 epilog="©Amir Hasanov all rights reserved")

parser.add_argument("-w", "--webui", action="store_true", help="Start webui (default on http://127.0.0.1:8080)")
parser.add_argument("--host", default=HOST, help="Set custom host")
parser.add_argument("--port", type=int, default=PORT, help="Set custom port")
parser.add_argument("--debug", type=bool, default=DEBUG, help="Set debug parametr to True")
parser.add_argument("-p", "--path", help="Set search path in cmd")

args = parser.parse_args()

if __name__ == "__main__":
    if args.webui:
        run_server(vars(args))
    elif args.path:
        run_serverless(args.path)
