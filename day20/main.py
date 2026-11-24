import cv2
import os

#出力先フォルダ
output_dir = "output"

#出力先フォルダが存在しない場合は作成
os.makedirs(output_dir, exist_ok=True)

#画像を読み込む
image = cv2.imread("sample01.jpg")

#画像が読み込めたか確認
if image is None:
    print("画像が読み込めませんでした。")
else:
    #画像の形状（高さ・幅・チャンネル数）を取得
    print(image.shape)

    height, width, channels = image.shape

    print(f"高さ：{height}")
    print(f"幅：{width}")
    print(f"チャンネル数：{channels}")

    #読み込んだ画像をそのまま保存
    output_path = os.path.join(output_dir, "output_original.jpg")

    if cv2.imwrite(output_path, image):
        print("画像の保存に成功しました。")
    else:
        print("画像の保存に失敗しました。")