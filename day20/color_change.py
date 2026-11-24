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
    #B(青)チャンネルを0にする
    brue_removed = image.copy()
    brue_removed[:,:,0] = 0

    #G(緑)チャンネルを0にする
    green_removed = image.copy()
    green_removed[:,:,1] = 0

    #R(赤)チャンネルを0にする
    red_removed = image.copy()
    red_removed[:,:,2] = 0

    #各チャンネルを変更した画像を保存
    cv2.imwrite(
        os.path.join(output_dir,"output_blue_removed.jpg"),
        brue_removed
    )

    cv2.imwrite(
        os.path.join(output_dir,"output_green_removed.jpg"),
        green_removed
    )

    cv2.imwrite(
        os.path.join(output_dir,"output_red_removed.jpg"),
        red_removed
    )

    print("チャンネル変更画像を保存しました。")