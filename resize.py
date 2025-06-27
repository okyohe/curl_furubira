from PIL import Image
import os

# 1. 対象画像ファイル名リスト
image_files = [
    "background_navy.png",
    "background_beige.webp",
    "background_kamui.png",
]

# 2. 元画像のディレクトリ
input_dir = r"C:\Users\yhwca\WorkSpace\古平町\curl_furubira_vue\src\assets\images\logo"

# 3. 横幅400pxでリサイズし、元ファイル名で上書き保存
# PIL.ImageのLANCZOSはバージョンによってはImage.Resampling.LANCZOS
try:
    resample = Image.Resampling.LANCZOS
except AttributeError:
    resample = Image.LANCZOS

target_width = 400

for filename in image_files:
    input_path = os.path.join(input_dir, filename)
    output_path = input_path  # 上書き保存
    if not os.path.exists(input_path):
        print(f"ファイルが見つかりません: {input_path}")
        continue
    with Image.open(input_path) as img:
        width, height = img.size
        scale = target_width / width
        new_height = int(height * scale)
        img_resized = img.resize((target_width, new_height), resample)
        img_resized.save(output_path, "PNG", optimize=True)
        print(f"リサイズ完了: {output_path} ({target_width}x{new_height})")

print("すべての画像をリサイズしました。")