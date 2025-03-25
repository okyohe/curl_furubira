from PIL import Image
import os

# 画像フォルダのパス
input_folder = r"C:\Users\yhwca\WorkSpace\curl_furubira\ws\src\assets\images\photos"
output_folder = os.path.join(input_folder, "resized")

# 出力フォルダを作成（存在しない場合）
os.makedirs(output_folder, exist_ok=True)

# 横幅1920pxを基準とする
target_width = 1920

# 画像を一括変換
for filename in os.listdir(input_folder):
    if filename.lower().endswith((".png", ".jpg", ".jpeg", ".webp")):  # 対象の画像フォーマット
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)

        # 元のサイズ
        width, height = img.size

        # アスペクト比を維持しつつ、横1920pxを基準にリサイズ
        scale_factor = target_width / width
        new_width = target_width
        new_height = int(height * scale_factor)

        # リサイズ処理
        img_resized = img.resize((new_width, new_height), Image.LANCZOS)

        # 保存（JPEG品質を85に設定して最適化）
        output_path = os.path.join(output_folder, filename)
        img_resized.save(output_path, quality=85)

        print(f"リサイズ完了: {output_path} ({new_width}x{new_height})")

print("すべての画像をリサイズしました。")
