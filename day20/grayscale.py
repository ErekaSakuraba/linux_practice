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

    #グレースケール画像を保存
    cv2.imwrite(
        os.path.join(output_dir,"output_gray.jpg"),
        gray_image
    )

    #元画像の色を反転
    #各画素の値を255から引く
    inverted_image = 255 - image

    #色反転画像を保存
    cv2.imwrite(
        os.path.join(output_dir,"output_invert.jpg"),
        inverted_image
    )

    print("グレースケール・色反転画像を保存しました。")