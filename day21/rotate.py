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
    #時計回りに90度回転
    rotate_90 = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

    #反時計回りに90度回転
    rotate_270 = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)

    #180度回転
    rotate_180 = cv2.rotate(image, cv2.ROTATE_180)

    #各回転画像を保存
    cv2.imwrite(
        os.path.join(output_dir, "output_rotate_90.jpg"),
        rotate_90
    )

    cv2.imwrite(
        os.path.join(output_dir, "output_rotate_270.jpg"),
        rotate_270
    )

    cv2.imwrite(
        os.path.join(output_dir, "output_rotate_180.jpg"),
        rotate_180
    )

    print("回転画像を保存しました。")