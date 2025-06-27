from PIL import Image
import os

# Pillowのバージョン差を吸収
try:
    resample_filter = Image.Resampling.LANCZOS
except AttributeError:
    resample_filter = Image.LANCZOS  # type: ignore

# 変換対象の画像ファイル名
image_files = [
    "background_navy.png",
    "background_beige.webp",
    "background_kamui.png",
    "boxlogo_white.png",
    "boxlogo_navy.webp",
]

# 画像が格納されているディレクトリ
image_dir = "src/assets/images/logo"

# モバイル版の接尾辞
mobile_suffix = "-mobile"

# モバイル版リサイズ時のターゲット幅
target_width = 200

# WebPの品質設定
webp_quality = 80

for filename in image_files:
    if not filename.endswith(".png"):
        print(f"PNG以外のファイルはスキップします: {filename}")
        continue

    name, _ = os.path.splitext(filename)
    input_path = os.path.join(image_dir, filename)

    if not os.path.exists(input_path):
        print(f"ファイルが見つかりません: {input_path}")
        continue

    try:
        with Image.open(input_path) as img:
            # 1. デスクトップ版 WebP を生成
            desktop_webp_path = os.path.join(image_dir, f"{name}.webp")
            img.save(desktop_webp_path, "WEBP", quality=webp_quality)

            original_size = os.path.getsize(input_path)
            desktop_webp_size = os.path.getsize(desktop_webp_path)
            desktop_reduction = (original_size - desktop_webp_size) / original_size * 100 if original_size > 0 else 0

            print(f"作成完了 (Desktop): {desktop_webp_path}")
            print(f"  PNGサイズ: {original_size / 1024:.2f} KB -> WebPサイズ: {desktop_webp_size / 1024:.2f} KB (削減率: {desktop_reduction:.2f}%)")

            # 2. モバイル版 WebP を生成
            mobile_webp_path = os.path.join(image_dir, f"{name}{mobile_suffix}.webp")

            img_for_mobile = img
            # 背景画像の場合はリサイズ
            if name.startswith("background"):
                width, height = img.size
                if width > target_width:
                    scale = target_width / width
                    new_height = int(height * scale)
                    img_for_mobile = img.resize((target_width, new_height), resample_filter)

            img_for_mobile.save(mobile_webp_path, "WEBP", quality=webp_quality)

            mobile_webp_size = os.path.getsize(mobile_webp_path)
            mobile_reduction = (original_size - mobile_webp_size) / original_size * 100 if original_size > 0 else 0

            print(f"作成完了 (Mobile): {mobile_webp_path}")
            print(f"  PNGサイズ: {original_size / 1024:.2f} KB -> WebPサイズ: {mobile_webp_size / 1024:.2f} KB (削減率: {mobile_reduction:.2f}%)")
            print("-" * 20)

    except Exception as e:
        print(f"エラーが発生しました ({filename}): {e}")

print("\nすべての画像のWebP変換処理が完了しました。")

# 不要になったモバイルPNGファイルを削除
print("\n古いモバイルPNGファイルを削除します...")
for filename in image_files:
    name, _ = os.path.splitext(filename)
    mobile_png_path = os.path.join(image_dir, f"{name}{mobile_suffix}.png")
    if os.path.exists(mobile_png_path):
        try:
            os.remove(mobile_png_path)
            print(f"削除しました: {mobile_png_path}")
        except OSError as e:
            print(f"エラーが発生しました ({mobile_png_path}の削除時): {e}") 