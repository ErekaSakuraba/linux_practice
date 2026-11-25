import cv2
import os

#出力先フォルダ
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

#画像を読み込む
image = cv2.imread("sample02.jpg")

if image is None:
    print("画像を読み込めませんでした。")
else:
    #左右反転
    flip_lr = cv2.flip(image,1)

    #上下反転
    flip_tb = cv2.flip(image, 0)

    #上下左右反転
    flip_all = cv2.flip(image, -1)

    #各各反転画像を保存
    cv2.imwrite(
        os.path.join(output_dir, "output_flip_horizontal.jpg"),
        flip_lr
    )

    cv2.imwrite(
        os.path.join(output_dir, "output_flip_vertical.jpg"),
        flip_tb
    )

    cv2.imwrite(
        os.path.join(output_dir, "output_flip_both.jpg"),
        flip_all
    )

    print("反転画像を保存しました。")