from PIL import Image
import os

# 画像フォルダのパス
input_folder = r"C:\Users\yhwca\WorkSpace\古平町\curl_furubira_vue\src\assets\images\photos"
output_folder = os.path.join(input_folder, "resized")

# 出力フォルダを作成（存在しない場合）
os.makedirs(output_folder, exist_ok=True)

# 横幅800pxを基準とする
target_width = 800

# 画像を一括変換
for filename in os.listdir(input_folder):
    if filename.lower().endswith((".png", ".jpg", ".jpeg")):  # 対象の画像フォーマット
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)

        # 元のサイズ
        width, height = img.size

        # アスペクト比を維持しつつ、横800pxを基準にリサイズ
        scale_factor = target_width / width
        new_width = target_width
        new_height = int(height * scale_factor)

        # リサイズ処理
        img_resized = img.resize((new_width, new_height), Image.LANCZOS)

        # JPEG品質を70に設定して最適化
        output_path = os.path.join(output_folder, filename)
        img_resized.save(output_path, quality=70, optimize=True)

        # WebP形式でも保存（必要なら）
        webp_path = os.path.splitext(output_path)[0] + ".webp"
        img_resized.save(webp_path, "WEBP", quality=70, optimize=True)

        print(f"リサイズ完了: {output_path} ({new_width}x{new_height})")
        print(f"WebP保存: {webp_path}")

print("すべての画像をリサイズしました。")
