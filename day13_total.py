import logging
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    filename="day14.log",
    encoding="utf-8"
)

def read_logs(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.readlines()
    except FileNotFoundError:
        logging.exception("ログファイルの読み込みに失敗しました")
        return []

