import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(message)s",
    filename="day13.log",
    encoding="utf-8",
    filemode="w"
)

logging.debug("デバッグ情報")
logging.info("処理を開始しました")
logging.warning("処理に時間がかかっています")
logging.error("Database接続に失敗しました")
logging.critical("システム停止")