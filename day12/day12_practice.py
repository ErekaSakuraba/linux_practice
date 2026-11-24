
from datetime import datetime

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
        continue

    try:
        log_time = datetime.strptime(
            parts[0] + " " + parts[1],
            "%Y-%m-%d %H:%M:%S"
        )
    except ValueError:
        continue

    if log_time >= target_time and parts[2] == "ERROR":
        error_count[parts[3]] = error_count.get(parts[3], 0) + 1


print("該当するログ件数：", sum(error_count.values()))
for error_type, count in error_count.items():
    print(f"{error_type}: {count}")

ranking = sorted(
    error_count.items(),
    key=lambda item: item[1],
    reverse=True
)

print("\nERRORランキング")
for name, count in ranking:
    print(f"{name}：{count}件")