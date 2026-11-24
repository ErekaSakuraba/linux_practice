with open("system.log", "r", encoding="utf-8") as file:
    logs = file.readlines()

print("ログの総行数：", len(logs))

error_count = {}
warn_count = {}

for line in logs:
    parts = line.split()

    if len(parts) < 4:
        continue

    level = parts[2]
    target = parts[3]

    if level == "ERROR":
        error_count[target] = error_count.get(target, 0) + 1

    elif level == "WARN":
        warn_count[target] = warn_count.get(target, 0) + 1

print("ERROR件数：", error_count)
print("WARN件数：", warn_count)

print("\nERRORランキング")

error_ranking = sorted(
    error_count.items(),
    key=lambda item: item[1],
    reverse=True
)

for name, count in error_ranking:
    print(f"{name}：{count}件")

print("\nWARNランキング")

warn_ranking = sorted(
    warn_count.items(),
    key=lambda item: item[1],
    reverse=True
)

for name, count in warn_ranking:
    print(f"{name}：{count}件")

with open("analysis_result.txt", "w", encoding="utf-8") as file:
    file.write("ログ解析結果\n")
    file.write(f"総行数：{len(logs)}\n\n")

    file.write("ERRORランキング\n")
    for name, count in error_ranking:
        file.write(f"{name}：{count}件\n")

    file.write("\nWARNランキング\n")
    for name, count in warn_ranking:
        file.write(f"{name}：{count}件\n")

print("解析結果を保存しました！")