from wand.image import Image
with Image(filename='color.jpg') as img:
	img.type = 'grayscale';
	img.save(filename='grayscale.jpg');