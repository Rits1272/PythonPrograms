import cv2 as cv

    # Read image
original_image = cv.imread("C:/Users/RITs/Desktop/Old stuff/image.jpeg")

    # Convert color image to grayscale for viola-jones
grayscale_image = cv.cvtColor(original_image, cv.COLOR_BGR2GRAY)

    # Load the classifier and create a cascade object for face detection
face_cascade = cv.CascadeClassifier('C:/Users/RITs/Desktop/Old stuff/myBlog/myvenv/Lib/site-packages/cv2/data/haarcascade_frontalface_alt.xml')

    # The term MultiScale indicates that the algorithm looks
    # at subregions of the image in multiple scales, to detect
    # faces of varying sizes:
detected_face = face_cascade.detectMultiScale(grayscale_image)

for (column, row, width, height) in detected_face:
    cv.rectangle(
    original_image,
    (column, row),
    (column + width, row + height),
    (0, 255, 0),
    2
    )

    #  Displaying the image
cv.imshow('Image', original_image)
cv.waitKey(0)
cv.destroyAllWindows()
