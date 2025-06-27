import os
from PIL import Image

def create_mobile_versions():
    # 画像が格納されているディレクトリ
    input_dir = "src/assets/images/logo/"
    
    # 対象の画像ファイル
    target_files = ["background_beige.webp", "background_navy.webp"]
    
    # Pillowがインストールされているか確認
    try:
        from PIL import Image
    except ImportError:
        print("Pillowがインストールされていません。")
        print("pip install Pillow を実行してください。")
        return

    print("モバイル版画像の作成を開始します...")
    for image_file in target_files:
        try:
            # 入力ファイルパス
            input_path = os.path.join(input_dir, image_file)
            
            # 画像を開く
            with Image.open(input_path) as img:
                # 元の画像サイズ
                width, height = img.size
                
                # 新しい幅を計算 (元の1/10)
                new_width = width // 10
                
                # アスペクト比を維持した新しい高さを計算
                new_height = int(new_width * (height / width))
                
                # 画像をリサイズ
                resized_img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
                
                # 出力ファイルパスを作成
                file_name, file_ext = os.path.splitext(image_file)
                output_filename = f"{file_name}-mobile{file_ext}"
                output_path = os.path.join(input_dir, output_filename)
                
                # 画像を保存
                resized_img.save(output_path, 'WEBP')
                
                print(f"'{output_path}' を幅{new_width}pxで作成しました。")

        except FileNotFoundError:
            print(f"エラー: ファイル '{input_path}' が見つかりませんでした。")
        except Exception as e:
            print(f"'{image_file}' の処理中にエラーが発生しました: {e}")
    print("画像の処理が完了しました。")


if __name__ == "__main__":
    create_mobile_versions() 