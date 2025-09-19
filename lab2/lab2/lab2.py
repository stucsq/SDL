import os
import time
import logging
import psycopg

db_host = os.getenv("db_host")
db_port = int(os.getenv("db_port"))
db_name = os.getenv("db_name")
db_user = os.getenv("db_user")
db_password = os.getenv("db_password")
interval = int(os.getenv("interval_seconds"))
log_file = os.getenv("log_file")

handlers = [logging.StreamHandler()]
if log_file:
    handlers.append(logging.FileHandler(log_file))
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s", handlers=handlers)

while True:
    try:
        conn = psycopg.connect(
            host=db_host,
            port=db_port,
            dbname=db_name,
            user=db_user,
            password=db_password,
            connect_timeout=5
        )
        cur = conn.cursor()
        cur.execute("SELECT VERSION();")
        version = cur.fetchone()[0]
        logging.info(f"db version: {version}")
        cur.close()
        conn.close()
    except Exception as e:
        logging.error(f"connection failed: {e}")
        logging.info("retrying")
        time.sleep(5)
        continue

    time.sleep(interval)
