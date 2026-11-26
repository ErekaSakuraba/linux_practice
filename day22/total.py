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
    flip_lr = cv2.flip(image,1)

    #上下反転
    flip_tb = cv2.flip(image, 0)

    #上下左右反転
    flip_all = cv2.flip(image, -1)

    #複合加工
    crop_combi_image = image[300:700, 500:1000]
    resize_combi_image = cv2.resize(crop_combi_image, (300, 200))
    rotate_combi_image = cv2.rotate(resize_combi_image, cv2.ROTATE_90_CLOCKWISE)

    images = {
    "output_resize.jpg": resize_image,
    "output_crop.jpg": crop_image,
    "output_rotate_90.jpg" : rotate_image,
    "output_flip_horizontal.jpg" : flip_lr,
    "output_flip_vertical.jpg" : flip_tb,
    "output_flip_both.jpg" : flip_all,
    "output_combined.jpg" : rotate_combi_image
    }

    #保存処理
    for file_name, img in images.items():
        output_path = os.path.join(output_dir, file_name)
        if cv2.imwrite(output_path, img):
            print(f"{file_name} の保存に成功しました。")
            print(img.shape)
        else:
            print("画像の保存に失敗しました。")