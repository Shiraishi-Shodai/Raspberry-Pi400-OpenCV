import cv2

img = cv2.imread('cat.png')

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
while True:
    cv2.imshow('img', gray_img)
    
    # qキーが押されると、ウィンドウを閉じる
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
# cv2.waitKey(60000)
cv2.destroyAllwindows()