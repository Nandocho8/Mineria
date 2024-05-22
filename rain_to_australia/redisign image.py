from PIL import Image

# Open the uploaded image
image_path = "./sidney.jpg"
image = Image.open(image_path)

# Resize the image to 1980x1400 pixels
resized_image = image.resize((1400, 400))
resized_image_path = "./aust2.jpg"
resized_image.save(resized_image_path)

resized_image_path