# 要傳入兩個parameter
# 一個是圖片的資料夾 pokedex/
# 一個是新建立的資料夾要來存放新的照片 new/

import sys
import os
from PIL import Image

# grab first and second argument
image_folder = sys.argv[1]
output_folder = sys.argv[2]
print(image_folder, output_folder)

# check is new/ exists, if not create
if not os.path.exists(output_folder):
    os.mkdir(output_folder)

# loop through Pokedex
# convert images to png
# save to the new folder
for filename in os.listdir(image_folder):
    if "jpg" in filename:
        img = Image.open(f"{image_folder}{filename}")
        # 可以把檔名跟extention拆開變成tuple
        # e.g. ('bulbasaur', '.jpg')
        clean_filename = os.path.splitext(filename)
        print(clean_filename)
        img.save(f"{output_folder}{clean_filename[0]}.png","png")
        print("all done")


