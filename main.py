# encode utf-8

import MetaTrader5 as mt5
from datetime import datetime
import pandas as pd
import pytz

from config import LOGIN, PASSWORD, SERVER, TICKETS, RETRIEVE_TICKETS_SINCE


def main():
    # Initialize MetaTrader 5 connection
    if not mt5.initialize():
        mt5.shutdown()
        print("initialize() failed, error code =", mt5.last_error())
        raise Exception("login failed")

    print("MetaTrader 5 initialized successfully")
    # Get the current time
    timezone = pytz.timezone("America/Sao_Paulo")
    utc_from = datetime(2020, 1, 10, tzinfo=timezone)
    utc_to = datetime(2020, 1, 11, hour=13, tzinfo=timezone)

    print("Retrieving tickets since %s" % utc_from)
    print("Retrieving tickets until %s" % utc_to)

    # Create a DataFrame to store the results
    df = pd.DataFrame(columns=["Ticket", "Profit"])

    # Loop through each ticket and get the profit
    for ticket in TICKETS:
        try:
            print("Retrieving profit for ticket %s" % ticket)
            candles = mt5.copy_rates_range(
                "BOVA11",
                mt5.TIMEFRAME_M5,
                utc_from,
                utc_to,
            )
        except Exception as e:
            print("Error retrieving candles for ticket %s: %s" % (ticket, e))
            continue

        print("Candles retrieved for ticket %s" % candles)

        if candles is None:
            print("No candles found for ticket %s" % ticket)
            continue

        df_candles = pd.DataFrame(candles)

        # save to file
        df_candles.to_csv("candles_%s.csv" % ticket, index=False)

    # Shutdown MetaTrader 5 connection
    mt5.shutdown()


if __name__ == "__main__":
    print("Starting script")
    try:
        main()
    except Exception as e:
        print("Ending in ERROR: %s", e)
    print("Ending script")
