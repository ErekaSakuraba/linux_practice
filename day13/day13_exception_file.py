import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    filename="day13_file_error.log",
    encoding="utf-8"
)

logging.info("ファイル読み込みを開始します")

try:
    with open("missing_file.txt", "r", encoding="utf-8") as file:
        data = file.read()

except FileNotFoundError:
    logging.exception("ファイル読み込みに失敗しました")

logging.info("処理を終了します")