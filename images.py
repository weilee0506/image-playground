from PIL import Image, ImageFilter

img = Image.open("./pokedex/pikachu.jpg")

# filter可以加一些效果
filtered_img = img.filter(ImageFilter.BLUR)
# convert可以轉換format，比如說轉換成grey scale
converted_img = img.convert('L')
# rotate可以旋轉
rotated_img = img.rotate(90)
# resize可以重新調整大小
resized_img = img.resize((200,200))
# crop可以裁剪
box = (100,100,400,400)
cropped_img = img.crop(box)

# 轉成png是因為他支援ImageFilter
# save存成圖片
filtered_img.save("blur.png","png")
converted_img.save("grey.png","png")
rotated_img.save("rotate.png","png")
resized_img.save("resized.png","png")
cropped_img.save("cropped.png","png")
print(img.size)



img2 = Image.open("./astro.jpg")
print(img2.size)

resized_img2 = img2.resize((400,200))
# thumbnail會在保持長寬比例的狀況下調整大小，所以最後結果不一定會是(400,200)
# thumbnail不會return一個新的圖，而是會去改舊的
img2.thumbnail((400,200))


resized_img2.save("resized_img2.png","png")
img2.save("img2.png","png")
