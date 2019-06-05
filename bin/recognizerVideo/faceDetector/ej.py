import cv2

# img = cv2.imread("example2.jpg")

img = cv2.imread("example1.jpg")


cv2.imshow("real",img)

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(img)
cv2.imshow("nuevol",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
