import logging
from datetime import datetime

from log_utils import create_ranking

error_count = {
    "Camera": 5,
    "Database": 8,
    "Network": 3
}

created_ranking = create_ranking(error_count)

print("ERRORランキング")
for rank, (error_type, count) in enumerate(created_ranking, start=1):
    print(f"{rank}位: {error_type} - {count}件")