import cv2

img = cv2.imread('./tmp/lena.jpg')

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()