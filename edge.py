import cv2

img = cv2.imread('cat.png')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# cv2.Canny(画像、ノイズの許容値、エッジの検出可能値)
edges = cv2.Canny(gray_img, 50, 100)
cv2.imshow('img', edges)
cv2.waitKey(0)