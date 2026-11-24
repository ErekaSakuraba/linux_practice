import logging
from datetime import datetime

from log_utils import read_logs, analyze_logs, create_ranking, output_results

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    filename="day15.log",
    encoding="utf-8"
)

def main():
    logging.info("ログ分析を開始します")

    logs = read_logs("system.log")

    target_time = datetime.strptime(
        "2026-11-16 09:02:00",
        "%Y-%m-%d %H:%M:%S"
    )

    error_count = analyze_logs(logs, target_time)
    ranking = create_ranking(error_count)
    output_results(error_count, ranking)

    logging.info("ログ分析を終了します")

if __name__ == "__main__":
    main()