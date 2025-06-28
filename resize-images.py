import os
from PIL import Image
import sys

def resize_images_to_webp(input_dir, output_dir, target_width=400, quality=80):
    """
    指定されたディレクトリ内の画像をリサイズし、WebP形式で保存する。

    :param input_dir: 入力画像のディレクトリ
    :param output_dir: 出力画像のディレクトリ
    :param target_width: リサイズ後の幅 (px)
    :param quality: WebPの品質 (0-100)
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"作成されたディレクトリ: {output_dir}")

    # 対応する拡張子
    supported_formats = ['.jpg', '.jpeg', '.png']

    for filename in os.listdir(input_dir):
        file_path = os.path.join(input_dir, filename)
        if os.path.isfile(file_path):
            ext = os.path.splitext(filename)[1].lower()
            if ext in supported_formats:
                try:
                    with Image.open(file_path) as img:
                        # アルファチャンネルを持つかチェック
                        has_alpha = img.mode in ('RGBA', 'LA', 'P')
                        
                        # アスペクト比を維持してリサイズ
                        width, height = img.size
                        aspect_ratio = height / width
                        new_height = int(target_width * aspect_ratio)
                        
                        resized_img = img.resize((target_width, new_height), Image.Resampling.LANCZOS)

                        # 新しいファイル名 (拡張子を .webp に変更)
                        base_filename = os.path.splitext(filename)[0]
                        new_filename = f"{base_filename}.webp"
                        output_path = os.path.join(output_dir, new_filename)

                        # WebPで保存
                        resized_img.save(output_path, 'WEBP', quality=quality, lossless=False, method=6)
                        
                        print(f"変換完了: {file_path} -> {output_path}")

                except Exception as e:
                    print(f"エラー: {filename} の処理中にエラーが発生しました: {e}", file=sys.stderr)

if __name__ == "__main__":
    # photosディレクトリの画像をリサイズ
    input_photos_dir = "src/assets/images/photos"
    output_photos_dir = "src/assets/images/photos" 
    print(f"\n'{input_photos_dir}' 内の画像を処理中...")
    resize_images_to_webp(input_photos_dir, output_photos_dir)

    # logoディレクトリの画像をリサイズ
    input_logo_dir = "src/assets/images/logo"
    output_logo_dir = "src/assets/images/logo"
    print(f"\n'{input_logo_dir}' 内の画像を処理中...")
    resize_images_to_webp(input_logo_dir, output_logo_dir)

    print("\nすべての画像の処理が完了しました。") 