import os
from PIL import Image

# 変換対象ディレクトリリスト
target_dirs = [
    r"C:\Users\yhwca\WorkSpace\古平町\curl_furubira_vue\src\assets\images\photos",
    r"C:\Users\yhwca\WorkSpace\古平町\curl_furubira_vue\src\assets\images\logo",
    r"C:\Users\yhwca\WorkSpace\古平町\curl_furubira_vue\src\assets\images\generated",
]

count = 0
for folder in target_dirs:
    for filename in os.listdir(folder):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            img_path = os.path.join(folder, filename)
            img = Image.open(img_path).convert("RGB")
            webp_path = os.path.splitext(img_path)[0] + ".webp"
            img.save(webp_path, "WEBP", quality=80, optimize=True)
            print(f"変換: {img_path} → {webp_path}")
            count += 1

print(f"WebP変換完了: {count}枚")