import os
from PIL import Image

input_folder = r"C:\Users\yhwca\WorkSpace\古平町\curl_furubira_vue\src\assets\images\photos"

count = 0
for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path).convert("RGB")
        webp_path = os.path.splitext(img_path)[0] + ".webp"
        img.save(webp_path, "WEBP", quality=80, optimize=True)
        print(f"変換: {filename} → {os.path.basename(webp_path)}")
        count += 1

print(f"WebP変換完了: {count}枚")
