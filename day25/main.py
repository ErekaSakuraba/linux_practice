import cv2
import numpy as np
import os

# 出力先フォルダ
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

# 画像を読み込む
image = cv2.imread("sample02.jpg")

if image is None:
    print("画像を読み込めませんでした。")
else:
    # グレースケール変換
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 二値化
    _, binary_image = cv2.threshold(
        gray_image, 150, 255, cv2.THRESH_BINARY
    )

    # 二値画像を保存
    cv2.imwrite(
        os.path.join(output_dir, "output_binary.jpg"),
        binary_image
    )

    #輪郭検出(外側の輪郭のみ取得)
    contours, hierarcy = cv2.findContours(
        binary_image,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )
    print(f"検出した輪郭数：{len(contours)}")
    
    # 輪郭の面積を取得
    areas = [cv2.contourArea(contour) for contour in contours]
    # 面積が最大の輪郭のインデックスを取得
    max_index = np.argmax(areas)

    # 最大の輪郭の面積を表示
    print(f"最大輪郭の面積：{areas[max_index]}")

    # 面積が一定以上の輪郭だけ描画
    contour_image = image.copy()

    # 面積が一定以上の輪郭を選別
    min_area = 10000

    for contour in contours:
        area = cv2.contourArea(contour)

        if area >= min_area:
            # 外接矩形を取得
            x, y, w, h = cv2.boundingRect(contour)

            # 外接矩形を描画
            cv2.rectangle(
                contour_image,
                (x, y),
                (x + w, y + h),
                (0, 255, 0),
                2
            )

            # 面積・幅・高さを表示
            print(f"面積：{area:.1f}, 幅：{w}, 高さ：{h}")

    # 輪郭・外接矩形の描画結果を保存
    cv2.imwrite(
        os.path.join(output_dir, "output_contours.jpg"),
        contour_image
    )

    print("画像の保存に成功しました。")