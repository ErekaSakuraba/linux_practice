import configparser
import logging
import sys
from datetime import datetime

from log_utils import read_logs, analyze_logs, create_ranking, output_results

missing_options = []
config = configparser.ConfigParser()

if loaded_files := config.read("config.ini", encoding="utf-8"):
    if config.has_section("log"):
        print("設定ファイルの読み込みに成功しました")

        if not config.has_option("log", "file_name"):
            missing_options.append("file_name")
        if not config.has_option("log", "target_time"):
            missing_options.append("target_time")
        if not config.has_option("log", "output_file"):
            missing_options.append("output_file")

        if missing_options:
            print("以下の設定項目が不足しています:")
            for option in missing_options:
                print(f" - {option}")
            sys.exit(1)
        else:
            print("必要な設定項目はすべて揃っています")

    else:
        print("設定ファイルにlogセクションが存在しません")
        sys.exit(1)

else:
    print("設定ファイルの読み込みに失敗しました")
    sys.exit(1)

try:
    log_file_name = config.get("log", "file_name")
    target_time_str = config.get("log", "target_time")
    output_file_name = config.get("log", "output_file")

    target_time = datetime.strptime(
        target_time_str,
        "%Y-%m-%d %H:%M:%S"
    )
except configparser.NoOptionError as e:
    print(f"設定項目が見つかりません: {e}")
    sys.exit(1)
except ValueError as e:
    print(f"日時形式が不正です: {e}")
    sys.exit(1)

logs = read_logs(log_file_name)
if logs is None:
    print("ログファイルの読み込みに失敗したため、分析を中止します")
    sys.exit(1)