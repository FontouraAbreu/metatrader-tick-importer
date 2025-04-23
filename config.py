import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

LOGIN = os.getenv("LOGIN", "<LOGIN NOT CONFIGURED>")
PASSWORD = os.getenv("PASSWORD", "<PASSWORD NOT CONFIGURED>")
SERVER = os.getenv("SERVER", "<SERVER NOT CONFIGURED>")
TICKETS = os.getenv("TICKETS", "<TICKETS NOT CONFIGURED>")
RETRIEVE_TICKETS_SINCE = os.getenv(
    "RETRIEVE_TICKETS_SINCE", "<RETRIEVE_TICKETS_SINCE NOT CONFIGURED>"
)
# transform RETRIEVE_TICKETS_SINCE to datetime
RETRIEVE_TICKETS_SINCE = datetime.strptime(
    RETRIEVE_TICKETS_SINCE, "%Y-%m-%d %H:%M:%S"
).timestamp()
