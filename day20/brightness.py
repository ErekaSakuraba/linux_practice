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
    #画像を明るくする
    #各ピクセルに50を加算
    bright_image = cv2.add(image,50)

    #画像を暗くする
    #各ピクセルから50を減算
    dark_image = cv2.subtract(image,50)

    #明るい画像を保存
    cv2.imwrite(
        os.path.join(output_dir,"output_brght.jpg"),
        bright_image
    )

    #暗い画像を保存
    cv2.imwrite(
        os.path.join(output_dir,"output_dark.jpg"),
        dark_image
    )

    print("明るさ変更画像を保存しました。")