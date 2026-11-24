import logging
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    filename="day13_total.log",
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


def read_logs(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.readlines()
    except FileNotFoundError:
        logging.exception("ログファイルの読み込みに失敗しました")
        return []


def analyze_logs(log_lines, target_time):
    error_count = {}

    for line in log_lines:
        parts = line.split()

        if len(parts) < 4:
            logging.warning("不正なログ行をスキップします：%s", line.strip())
            continue

        if parts[2] != "ERROR":
            continue

        datetime_str = parts[0] + " " + parts[1]

        try:
            log_time = datetime.strptime(
                datetime_str,
                "%Y-%m-%d %H:%M:%S"
            )
        except ValueError:
            logging.warning("不正な日時をスキップします：%s", line.strip())
            continue

        if log_time >= target_time:
            error_count[parts[3]] = error_count.get(parts[3], 0) + 1

    return error_count


def create_ranking(error_count):
    ranking = sorted(
        error_count.items(),
        key=lambda item: item[1],
        reverse=True
    )
    return ranking


def output_results(error_count, ranking):
    logging.info("ERROR合計件数：%d", sum(error_count.values()))

    for error_type, count in error_count.items():
        logging.info("%s：%d", error_type, count)

    logging.info("ERRORランキング")

    for rank, (error_type, count) in enumerate(ranking, start=1):
        logging.info("%d位：%s：%d件", rank, error_type, count)


if __name__ == "__main__":
    main()