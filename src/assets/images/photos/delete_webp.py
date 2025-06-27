import os

# 削除対象のフォルダパス
target_folder = r"C:\Users\yhwca\WorkSpace\古平町\curl_furubira_vue\src\assets\images\photos"

# .webpファイルを一括削除
deleted = 0
for filename in os.listdir(target_folder):
    if filename.lower().endswith(".webp"):
        file_path = os.path.join(target_folder, filename)
        os.remove(file_path)
        print(f"削除: {file_path}")
        deleted += 1

print(f"削除完了: {deleted}個のwebpファイル")