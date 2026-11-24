import cv2

image = cv2.imread("sample01.jpg")

print(image)
print(image.shape)

height, width, channels = image.shape

print(f"高さ：{height}")
print(f"幅：{width}")
print(f"チャンネル数：{channels}")

cv2.imwrite("output.jpg", image)