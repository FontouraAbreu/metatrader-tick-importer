# encode utf-8

import MetaTrader5 as mt5
from datetime import datetime
import pandas as pd

from config import LOGIN, PASSWORD, SERVER, TICKETS, RETRIEVE_TICKETS_SINCE

print("Login: %s" % LOGIN)
print("Password: %s" % PASSWORD)
print("Server: %s" % SERVER)
print("Tickets: %s" % TICKETS)


def main():
    # Initialize MetaTrader 5 connection
    if not mt5.initialize(login=LOGIN, password=PASSWORD, server=SERVER):
        print("initialize() failed")
        mt5.shutdown()
        raise Exception(
            "login failed, check your login credentials: %s" % mt5.last_error()
        )

    # Get the current time
    now = datetime.now()

    # Create a DataFrame to store the results
    df = pd.DataFrame(columns=["Ticket", "Profit"])

    # Loop through each ticket and get the profit
    for ticket in TICKETS:
        try:
            candles = mt5.copy_rates_range(
                ticket,
                mt5.TIMEFRAME_M1,
                now.replace(hour=0, minute=0, second=0, microsecond=0),
                datetime(RETRIEVE_TICKETS_SINCE),
            )
        except Exception as e:
            print("Error retrieving candles for ticket %s: %s" % (ticket, e))
            continue

        if candles is None:
            print("No candles found for ticket %s" % ticket)
            continue

        df_candles = pd.DataFrame(candles)

        # save to file
        df_candles.to_csv("candles_%s.csv" % ticket, index=False)

    # Shutdown MetaTrader 5 connection
    mt5.shutdown()


if __name__ == "main":
    print("Starting script")
    try:
        main()
    except Exception as e:
        print("Ending in ERROR: %s", e)
    print("Ending script")
