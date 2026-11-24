import cv2

image = cv2.imread("sample02.jpg")

if image is None:
    print("画像が読み込めませんでした。")
else:
    print(image)
    print(image.shape)

    height, width, channels = image.shape

    print(f"高さ：{height}")
    print(f"幅：{width}")
    print(f"チャンネル数：{channels}")

    if cv2.imwrite("output.jpg", image):
        print("画像の保存に成功しました。")
    else:
        print("画像の保存に失敗しました。")