import numpy as np
import cv2
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
    blur_3_image = cv2.blur(image, (3, 3))
    blur_15_image = cv2.blur(image, (15, 15))
    gaussian_3_image = cv2.GaussianBlur(image, (3, 3), 0)
    gaussian_15_image = cv2.GaussianBlur(image, (15, 15), 0)
    gaussian_31_image = cv2.GaussianBlur(image, (31, 31), 0)
    gaussian_sigma_5 = cv2.GaussianBlur(image, (15, 15), 5)
    gaussian_sigma_10 = cv2.GaussianBlur(image, (15, 15), 10)

    #ノイズの生成
    noise = np.random.normal(0, 25, image.shape)
    # ノイズを加えた画像を作成
    noise_image = np.clip(image + noise, 0, 255).astype(np.uint8)
    # ノイズをぼかして軽減
    noise_image_5 = cv2.GaussianBlur(noise_image, (5, 5), 0)

    #ソルト＆ペッパーノイズを作成
    sp_image = image.copy()
    #ランダムな座標を生成
    noise_y = np.random.randint(0,image.shape[0],5000)
    noise_x = np.random.randint(0,image.shape[1],5000)
    #白いノイズを追加
    sp_image[noise_y,noise_x] = 255
    #メディアンフィルタでノイズを軽減
    median_image = cv2.medianBlur(sp_image,5)

    #グレースケールに変換
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #エッジ検出
    sobel_x = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=3)
    #表示・保存用に変換
    sobel_x_image = cv2.convertScaleAbs(sobel_x)
    sobel_y_image = cv2.convertScaleAbs(sobel_y)
    
    # X方向とY方向のエッジを合成
    sobel_combined = np.sqrt(sobel_x ** 2 + sobel_y ** 2)
    # 表示・保存用に変換
    sobel_combined_image = cv2.convertScaleAbs(sobel_combined)

    # Cannyエッジ検出
    canny_image = cv2.Canny(gray_image, 100, 200)
    # Cannyの閾値を変更して比較
    canny_50_150 = cv2.Canny(gray_image, 50, 150)
    canny_100_200 = cv2.Canny(gray_image, 100, 200)
    canny_150_300 = cv2.Canny(gray_image, 150, 300)

    # グレースケール画像をぼかす
    gray_blur = cv2.GaussianBlur(gray_image, (5, 5), 0)

    # ぼかした画像にCannyを適用
    canny_blur_image = cv2.Canny(gray_blur, 100, 200)

    # ノイズ画像をグレースケールに変換
    noise_gray = cv2.cvtColor(noise_image, cv2.COLOR_BGR2GRAY)

    # ノイズ画像に直接Cannyを適用
    canny_noise = cv2.Canny(noise_gray, 100, 200)

    # ノイズ画像をぼかす
    noise_gray_blur = cv2.GaussianBlur(noise_gray, (5, 5), 0)
    #ぼかしの強さ変更
    noise_gray_blur_3 = cv2.GaussianBlur(noise_gray,(3,3),0)
    noise_gray_blur_5 = cv2.GaussianBlur(noise_gray,(5,5),0)
    noise_gray_blur_15 = cv2.GaussianBlur(noise_gray,(15,15),0)

    # ぼかしたノイズ画像にCannyを適用
    canny_noise_blur = cv2.Canny(noise_gray_blur, 100, 200)
    canny_noise_blur_3 = cv2.Canny(noise_gray_blur_3, 100, 200)
    canny_noise_blur_5 = cv2.Canny(noise_gray_blur_5, 100, 200)
    canny_noise_blur_15 = cv2.Canny(noise_gray_blur_15, 100, 200)

    # Bilateral Filterでノイズを軽減
    bilateral_image = cv2.bilateralFilter(noise_image, 9, 75, 75)   
    # グレースケールに変換
    bilateral_gray = cv2.cvtColor(bilateral_image, cv2.COLOR_BGR2GRAY)
    # Cannyを適用
    canny_bilateral = cv2.Canny(bilateral_gray, 100, 200)

    # Bilateral Filterのパラメータを変更
    bilateral_5 = cv2.bilateralFilter(noise_image, 5, 30, 30)
    bilateral_9 = cv2.bilateralFilter(noise_image, 9, 75, 75)
    bilateral_15 = cv2.bilateralFilter(noise_image, 15, 150, 150)

    # Laplacianによるエッジ検出
    laplacian = cv2.Laplacian(gray_image, cv2.CV_64F)

    # 表示・保存用に変換
    laplacian_image = cv2.convertScaleAbs(laplacian)
    
    images = {
    "output_blur_3.jpg": blur_3_image,
    "output_blur_15.jpg": blur_15_image,
    "output_gaussian_3.jpg" : gaussian_3_image,
    "output_gaussian_15.jpg" : gaussian_15_image,
    "output_gaussian_31.jpg" : gaussian_31_image,
    "output_gaussian_sigma5.jpg" : gaussian_sigma_5,
    "output_gaussian_sigma10.jpg" : gaussian_sigma_10,
    "output_original.jpg": image,
    "output_noise.jpg": noise_image,
    "output_denoise.jpg": noise_image_5,
    "output_salt_pepper.jpg": sp_image,
    "output_median.jpg" : median_image,
    "output_sobel_x.jpg": sobel_x_image,
    "output_sobel_y.jpg": sobel_y_image,
    "output_sobel_combined.jpg": sobel_combined_image,
    "output_canny.jpg": canny_image,
    "output_canny_50_150.jpg": canny_50_150,
    "output_canny_100_200.jpg": canny_100_200,
    "output_canny_150_300.jpg": canny_150_300,
    "output_canny_blur.jpg": canny_blur_image,
    "output_canny_noise.jpg": canny_noise,
    "output_canny_noise_blur.jpg": canny_noise_blur,
    "output_canny_noise_3.jpg": canny_noise_blur_3,
    "output_canny_noise_5.jpg": canny_noise_blur_5,
    "output_canny_noise_15.jpg": canny_noise_blur_15,
    "output_bilateral.jpg": bilateral_image,
    "output_canny_bilateral.jpg": canny_bilateral,
    "output_bilateral_5.jpg": bilateral_5,
    "output_bilateral_9.jpg": bilateral_9,
    "output_bilateral_15.jpg": bilateral_15,
    "output_laplacian.jpg": laplacian_image,
    }

    #保存処理
    for file_name, img in images.items():
        output_path = os.path.join(output_dir, file_name)
        if cv2.imwrite(output_path, img):
            print(f"{file_name} の保存に成功しました。")
            print(img.shape)
        else:
            print("画像の保存に失敗しました。")