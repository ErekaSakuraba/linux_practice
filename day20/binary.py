import cv2
import os

# 出力先フォルダ
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

# 画像を読み込む
image = cv2.imread("sample01.jpg")

if image is None:
    print("画像を読み込めませんでした。")
else:
    #カラー画像をグレースケールに変換
    gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    #閾値150、最大値255で二値化
    threshold_value,binary_image = cv2.threshold(
        gray_image,
        150,
        255,
        cv2.THRESH_BINARY
    )

    #二値化画像を保存
    cv2.imwrite(
        os.path.join(output_dir, "output_binary.jpg"),
        binary_image
    )

    print(f"設定した閾値：{threshold_value}")
    print("二値化画像を保存しました。")