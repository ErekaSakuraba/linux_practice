#①ログを読み込む関数
def read_logs():
    with open("system.log","r",encoding="utf-8") as file:
        logs = file.readlines()

    return logs

#②ログを解析・集計する関数
def analyze_logs(logs):
    error_count = {}
    warn_count = {}

    for line in logs:
        try:
            parts = line.split()
            level = parts[2]
            target = parts[3]

        except IndexError:
            print("不正なログをスキップ:", line.strip())
            continue

        if level == "ERROR":
            error_count[target] = error_count.get(target, 0) + 1

        elif level == "WARN":
            warn_count[target] = warn_count.get(target, 0) + 1

    return error_count, warn_count

#③解析結果をファイルに保存する関数
def save_results(error_count,warn_count):
    with open("analysis_result.txt","a",encoding="utf-8") as file:

        file.write("ERROR件数\n")

        for name,count in error_count.items():
            file.write(f"{name}:{count}件\n")

        file.write("\nWARN件数\n")

        for name,count in warn_count.items():
            file.write(f"{name}:{count}件\n")

    print("解析結果を保存しました！")

def show_error_ranking(error_count):
    result = sorted(
        error_count.items(),
        key=lambda item: item[1],
        reverse=True
    )

    print("ERRORランキング")

    for name, count in result:
        print(f"{name}：{count}件")

def show_warn_ranking(warn_count):
    result = sorted(
        warn_count.items(),
        key=lambda item: item[1],
        reverse=True
    )

    print("WARNランキング")

    for name, count in result:
        print(f"{name}：{count}件")

def save_ranking(error_count, warn_count):
    with open("analysis_result.txt", "a", encoding="utf-8") as file:
        file.write("ERRORランキング\n")
        for name, count in sorted(error_count.items(), key=lambda item: item[1], reverse=True):
            file.write(f"{name}：{count}件\n")

        file.write("\nWARNランキング\n")
        for name, count in sorted(warn_count.items(), key=lambda item: item[1], reverse=True):
            file.write(f"{name}：{count}件\n")
    
    print("ランキング結果を保存しました！")

#④メイン処理：関数を順番に実行する
logs = read_logs()

error_count,warn_count = analyze_logs(logs)

print("ERROR件数：",error_count)
print("WARN件数：",warn_count)

save_results(error_count,warn_count)

show_error_ranking(error_count)

show_warn_ranking(warn_count)

save_ranking(error_count, warn_count)