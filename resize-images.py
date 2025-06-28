import os
from PIL import Image
import sys

def resize_and_save_webp(file_path, output_path, target_width, quality=80):
    """
    画像をリサイズしてWebP形式で保存する
    """
    try:
        if not os.path.exists(file_path):
            print(f"エラー: 入力ファイルが見つかりません {file_path}", file=sys.stderr)
            return

        with Image.open(file_path) as img:
            # アスペクト比を維持してリサイズ
            width, height = img.size
            if width != target_width:
                aspect_ratio = height / width
                new_height = int(target_width * aspect_ratio)
                resized_img = img.resize((target_width, new_height), Image.Resampling.LANCZOS)
            else:
                resized_img = img

            # 出力先のディレクトリが存在しない場合は作成
            output_dir = os.path.dirname(output_path)
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)

            # WebPで保存
            resized_img.save(output_path, 'WEBP', quality=quality, lossless=False, method=6)
            
            print(f"変換完了: {file_path} -> {output_path} (幅: {target_width}px)")

    except Exception as e:
        filename = os.path.basename(file_path)
        print(f"エラー: {filename} の処理中にエラーが発生しました: {e}", file=sys.stderr)

if __name__ == "__main__":
    
    # FVで使用する画像のパス
    image_dir = "src/assets/images/photos"
    fv_images = [
        "0_100_white_pillow.jpg",
        "0_101_dining.jpg",
        "0_103_navypillow.jpg"
    ]

    print("--- FV用画像のリサイズ処理を開始します ---")

    for img_name in fv_images:
        base_name, ext = os.path.splitext(img_name)
        input_path = os.path.join(image_dir, img_name)

        # デスクトップ版 (1280px)
        desktop_output_path = os.path.join(image_dir, f"{base_name}.webp")
        resize_and_save_webp(input_path, desktop_output_path, 1280)

        # モバイル版 (400px)
        mobile_output_path = os.path.join(image_dir, f"{base_name}-mobile.webp")
        resize_and_save_webp(input_path, mobile_output_path, 400)

    print("\n--- FV用画像の処理が完了しました ---") 