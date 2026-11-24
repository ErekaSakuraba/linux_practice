import cv2
import os

#出力先フォルダ
output_dir = "output"
os.makedirs(output_dir,exist_ok=True)

#画像を読み込む
image = cv2.imread("sample01.jpg")

if image is None:
    print("画像を読み込めませんでした。")
else:
    #指定した座標のピクセル情報を取得
    #行（高さ方向）100,列（幅方向）200
    pixel = image[100,200]
    print(f"取得したピクセル：{pixel}")

    #指定したピクセルを赤色に変更(BGR)
    image[100,200] = [0,0,255]

    #変更した画像を保存
    output_path = os.path.join(output_dir,"output_pixel.jpg")
    cv2.imwrite(output_path,image)

    print("ピクセル変更画像を保存しました。")

#範囲指定用に元画像を再読み込み
image = cv2.imread("sample01.jpg")

if image is not None:
    #画像の左上100×100の範囲を指定
    #行：0~99、列：0~99
    image[0:100,0:100] = [0,0,255]

    #範囲変更した画像を保存
    output_path = os.path.join(output_dir,"output_region.jpg")
    cv2.imwrite(output_path,image)

    print("範囲変更画像を保存しました。")