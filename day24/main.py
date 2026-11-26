import cv2
import numpy as np
import os

# 出力先フォルダ
output_dir = "output"

# 出力先フォルダが存在しない場合は作成
os.makedirs(output_dir, exist_ok=True)

# 画像を読み込む
image = cv2.imread("sample02.jpg")

if image is None:
    print("画像を読み込めませんでした。")
else:
    # グレースケールに変換
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 二値化
    _, binary_image = cv2.threshold(gray_image, 150, 255, cv2.THRESH_BINARY)
    # 閾値50
    _, binary_50 = cv2.threshold(gray_image, 50, 255, cv2.THRESH_BINARY)
    # 閾値200
    _, binary_200 = cv2.threshold(gray_image, 200, 255, cv2.THRESH_BINARY)

    # 収縮処理用のカーネルを作成
    kernel = np.ones((3, 3), np.uint8)

    # 収縮処理
    erosion_image = cv2.erode(binary_image, kernel, iterations=1)
    # 収縮を1回
    erosion_1 = cv2.erode(binary_image, kernel, iterations=1)
    # 収縮を2回
    erosion_2 = cv2.erode(binary_image, kernel, iterations=2)
    # 収縮を3回
    erosion_3 = cv2.erode(binary_image, kernel, iterations=3)

    # 膨張処理
    dilation_1 = cv2.dilate(binary_image, kernel, iterations=1)
    dilation_2 = cv2.dilate(binary_image, kernel, iterations=2)
    dilation_3 = cv2.dilate(binary_image, kernel, iterations=3)

    # Opening（収縮 → 膨張）
    opening_image = cv2.morphologyEx(
        binary_image, cv2.MORPH_OPEN, kernel
    )

    # Closing（膨張 → 収縮）
    closing_image = cv2.morphologyEx(
        binary_image, cv2.MORPH_CLOSE, kernel
    )

    # Closing（膨張 → 収縮）
    closing_5 = cv2.morphologyEx(
        binary_image,
        cv2.MORPH_CLOSE,
        np.ones((5, 5), np.uint8)
    )

    closing_9 = cv2.morphologyEx(
        binary_image,
        cv2.MORPH_CLOSE,
        np.ones((9, 9), np.uint8)
    )

    # Morphological Gradient（輪郭抽出）
    gradient_image = cv2.morphologyEx(
        binary_image,
        cv2.MORPH_GRADIENT,
        kernel
    )

    # Morphological Gradient（カーネルサイズ比較）
    gradient_3 = cv2.morphologyEx(
        binary_image, cv2.MORPH_GRADIENT, np.ones((3, 3), np.uint8)
    )

    gradient_5 = cv2.morphologyEx(
        binary_image, cv2.MORPH_GRADIENT, np.ones((5, 5), np.uint8)
    )

    gradient_9 = cv2.morphologyEx(
        binary_image, cv2.MORPH_GRADIENT, np.ones((9, 9), np.uint8)
    )

    # 保存
    images = {
        "output_gray.jpg": gray_image,
        "output_binary.jpg": binary_image,
        "output_binary_50.jpg": binary_50,
        "output_binary_200.jpg": binary_200,
        "output_erosion.jpg": erosion_image,
        "output_erosion_1.jpg": erosion_1,
        "output_erosion_2.jpg": erosion_2,
        "output_erosion_3.jpg": erosion_3,
        "output_dilation_1.jpg": dilation_1,
        "output_dilation_2.jpg": dilation_2,
        "output_dilation_3.jpg": dilation_3,
        "output_opening.jpg": opening_image,
        "output_closing.jpg": closing_image,
        "output_closing_5.jpg" : closing_5,
        "output_closing_9.jpg" : closing_9,
        "output_gradient.jpg": gradient_image,
        "output_gradient_3.jpg" : gradient_3,
        "output_gradient_5.jpg" : gradient_5,
        "output_gradient_9.jpg" : gradient_9,
    }

    for file_name, img in images.items():
        output_path = os.path.join(output_dir, file_name)

        if cv2.imwrite(output_path, img):
            print(f"{file_name} の保存に成功しました。")
        else:
            print("画像の保存に失敗しました。")