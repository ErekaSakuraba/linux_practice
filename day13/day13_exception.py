import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    filename="day13_error_handling.log",
    encoding="utf-8"
)

logging.info("処理開始")

try:
    result = int("abc")

except FileNotFoundError:
    logging.warning("ファイルが見つからないため処理をスキップします")

except Exception:
    logging.exception("予期しないエラーが発生しました")

logging.info("処理終了")