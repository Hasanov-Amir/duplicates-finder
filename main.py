import argparse

from server import run_server
from serverless import run_serverless
from config import HOST, PORT, DEBUG


parser = argparse.ArgumentParser(
    description="Finds file duplicates using hash.",
    epilog="©Amir Hasanov all rights reserved.\nSpecial thanks to Vagif Mammedov for helping with redux toolkit.",
    formatter_class=argparse.RawDescriptionHelpFormatter
)

parser.add_argument("-w", "--webui", action="store_true", help="Start webui (default on http://127.0.0.1:8080)")
parser.add_argument("--host", default=HOST, help="Set custom host")
parser.add_argument("--port", type=int, default=PORT, help="Set custom port")
parser.add_argument("--debug", type=bool, default=DEBUG, help="Set debug parameter to True")
parser.add_argument("-p", "--path", help="Set search path in cmd")

args = parser.parse_args()

if __name__ == "__main__":
    if args.webui:
        run_server(vars(args))
    elif args.path:
        run_serverless(args.path)
