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
    #リサイズ
    resize_image = cv2.resize(image, (300, 200))
    
    #切り抜き
    crop_image = image[300:700, 500:1000]

    #回転
    rotate_image = cv2.rotate(resize_image, cv2.ROTATE_90_CLOCKWISE)

    #左右反転

    #各画像を保存
    cv2.imwrite(
        os.path.join(output_dir, "output_flip_horizontal.jpg"),
        resize_image
    )
    cv2.imwrite(
        os.path.join(output_dir, "output_flip_horizontal.jpg"),
        crop_image
    )
    cv2.imwrite(
        os.path.join(output_dir, "output_flip_horizontal.jpg"),
        rotate_image
    )

    output_path = os.path.join(output_dir, "output_combined.jpg")

    if cv2.imwrite(output_path, rotate_image):
        print("画像の保存に成功しました。")
        print(rotate_image.shape)
    else:
        print("画像の保存に失敗しました。")