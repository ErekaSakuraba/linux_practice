import cv2
import os

#出力先フォルダ
output_dir = "output"

#出力先フォルダが存在しない場合は作成
os.makedirs(output_dir, exist_ok=True)

#画像を読み込む
image = cv2.imread("sample02.jpg")

if image is None:
    print("画像を読み込めませんでした。")
else:
    
    resize_image = cv2.resize(image, (1000,500))

    #読み込んだ画像をそのまま保存
    output_path = os.path.join(output_dir, "output_resize.jpg")

    if cv2.imwrite(output_path, resize_image):
        print("画像の保存に成功しました。")
        print(resize_image.shape)
    else:
        print("画像の保存に失敗しました。")