import cv2
import sys 

picture = sys.argv[1]
prof_name = sys.argv[2]
# Read the image
img = cv2.imread(picture)
print(img.shape)
height = img.shape[0]
width = img.shape[1]

# Cut the image in half
height_cutoff = height // 2
s1 = img[:height_cutoff, :]
s2 = img[height_cutoff:, :]
# Save top half
cv2.imwrite(prof_name+".png", s1)