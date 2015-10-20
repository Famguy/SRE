import numpy as np
import svdrd as rd
import cv2

cap = cv2.VideoCapture('768x576.avi')

fgbg = cv2.createBackgroundSubtractorMOG2()

while(1):
	ret, frame = cap.read()

	fgmask = fgbg.apply(frame)

	print "frame"

	# end & show
	cv2.imshow('frame',fgmask)
	k = cv2.waitKey(30) & 0xff
	if k == 27:
		break

cap.release()
cv2.destroyAllWindows()


	