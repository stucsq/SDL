import json 
import getpass
import psycopg
import re


def load_config():
    with open("db_config.json", "r", encoding="utf-8") as f:
        config = json.load(f)
        return config

def get_creds():
    login = input("введи логин: ").strip()
    if not re.match(r"[a-zA-Z0-9_.]+", login):
        raise ValueError("Ошибка, вы ввели символы спец.символы")
    password = getpass.getpass("введи пароль: ")
    return login, password

def configure_conf(login,password,config):
    parameters = {}
    if "host" in config:
        parameters["host"] = config["host"]
    if "port" in config:
        parameters["port"] = config["port"]
    if "dbname" in config:
        parameters["dbname"] = config["dbname"]
    parameters["user"] = login
    parameters["password"] = password
    return parameters

def main():
    config = load_config()
    login, password = get_creds()
    parameters = configure_conf(login, password, config)
    try: 
        with psycopg.connect(**parameters) as connect:
            with connect.cursor() as curs:
                curs.execute("SELECT version();")
                print(curs.fetchone()[0])
    except Exception as e:
        print("Ошибка, подробнее:\n",e)

if __name__ == "__main__":
    main()

