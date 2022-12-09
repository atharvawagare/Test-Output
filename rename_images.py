# Documentation
# Author: Atharva Wagare (https://linkedin.com/in/atharvawagare)
# This file is for renaming all images in path directory to test1.jpeg, test2.jpg, test3.png .... and so on 
# Known working functions of os module to me are as follows
# os.mkdir("./renamed_images")
# os.rmdir("./renamed_images")
# os.rename("./12.png", "./test1.png")
# path="./images/"

def rename_images_in(path):
	import os

	images = os.listdir(path)

	i=1
	for img in images:
		new="test"+str(i)+"."
		os.rename(path+img, path+new+img.split(".")[-1])
		i+=1

rename_images_in("./images/")