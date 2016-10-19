def removeRed(imageWindow):
	newImageWindow = emptyImageWindow(imageWindow)
	for x in range(imageWidth(imageWindow)):
		for y in range(imageHeight(imageWindow)):
			rgb = pixelRGB(imageWindow, x, y)
			newRGB = [0, rgb[1], rgb[2]]
			setPixelRGB(newImageWindow, x, y, newRGB)
	return newImageWindow
