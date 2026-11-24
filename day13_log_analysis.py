import logging
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    filename="analysis.log",
    encoding="utf-8"
)

logging.info("ログ分析を開始します")

with open("system.log", "r", encoding="utf-8") as file:
    logs = file.readlines()

error_count = {}

target_time = datetime.strptime(
    "2026-11-16 09:02:00",
    "%Y-%m-%d %H:%M:%S"
)

for line in logs:
    parts = line.split()

    if len(parts) < 4:
        logging.warning("不正なログ行をスキップします：%s", line.strip())
        continue

    try:
        log_time = datetime.strptime(
            parts[0] + " " + parts[1],
            "%Y-%m-%d %H:%M:%S"
        )
    except ValueError:
        logging.warning("日時変換に失敗しました")
        continue

    if log_time >= target_time and parts[2] == "ERROR":
        error_count[parts[3]] = error_count.get(parts[3], 0) + 1

logging.info("ログ分析が完了しました")
logging.info("ERROR合計件数：%d", sum(error_count.values()))
for error_type, count in error_count.items():
    logging.info("%s：%d", error_type, count)
logging.info("ERRORランキング")
ranking = sorted(
    error_count.items(),
    key=lambda item: item[1],
    reverse=True
)
for rank, (error_type, count) in enumerate(ranking, start=1):
    logging.info("%d位：%s：%d件", rank, error_type, count)