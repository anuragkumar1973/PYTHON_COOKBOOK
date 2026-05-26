import argparse
import datetime
import logging
import schedule
import time
import sys
import threading
import os

#!/usr/bin/env python3
# /Users/anuragkumar1973/Downloads/book_py_cookbk/BOOK_PY_COOKBK/rec3_1.py



logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


def daily_report():
    """Task run every day at the scheduled time."""
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    logging.info("Generating daily report... (triggered at %s)", now)
    # TODO: replace the print/log above with real report generation logic


def parse_args():
    p = argparse.ArgumentParser(description="Daily report scheduler")
    p.add_argument(
        "--test",
        action="store_true",
        help="Run in test mode (job runs every 10 seconds instead of daily at 08:00)",
    )
    return p.parse_args()

def _start_input_listener():
    def _listener():
        logging.info("Input listener started. Type '0' and press Enter to stop the scheduler.")
        while True:
            try:
                s = input()
            except EOFError:
                break
            if s.strip() == "0":
                logging.info("Received '0' from user — exiting.")
                os._exit(0)
    t = threading.Thread(target=_listener, daemon=True)
    t.start()



def main():
    args = parse_args()

    if args.test:
        schedule.every(10).seconds.do(daily_report)
        sleep_interval = 1
        logging.info("Started in TEST mode: job scheduled every 10 seconds.")
        _start_input_listener()
    else:
        schedule.every().day.at("08:00").do(daily_report)
        sleep_interval = 60
        logging.info('Scheduled daily_report at 08:00 every day.')

    try:
        while True:
            schedule.run_pending()
            time.sleep(sleep_interval)
    except KeyboardInterrupt:
        logging.info("Scheduler stopped by user.")
        sys.exit(0)


if __name__ == "__main__":
    main()