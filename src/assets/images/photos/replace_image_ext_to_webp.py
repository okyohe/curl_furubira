import os
import re

# 1. /photos内の画像ファイル名リストを取得（拡張子除く）
photos_dir = r"C:\Users\yhwca\WorkSpace\古平町\curl_furubira_vue\src\assets\images\photos"
photo_basenames = set()
for fn in os.listdir(photos_dir):
    if fn.lower().endswith(('.jpg', '.jpeg', '.png')):
        photo_basenames.add(os.path.splitext(fn)[0])

# 2. プロジェクト全体で対象ファイル名だけ拡張子を.webpに置換
root_dir = r"C:\Users\yhwca\WorkSpace\古平町\curl_furubira_vue"
target_exts = (".vue", ".js", ".ts", ".html", ".css")

# ファイルリストを先に作成
all_files = []
for folder, _, files in os.walk(root_dir):
    for file in files:
        if file.endswith(target_exts):
            all_files.append(os.path.join(folder, file))

total_files = len(all_files)
replace_count = 0

for idx, path in enumerate(all_files, 1):
    print(f"[{idx}/{total_files}] {path} を処理中...")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    new_content = content
    file_replace = 0
    for basename in photo_basenames:
        # .jpg, .jpeg, .png → .webp
        new_content, n = re.subn(
            rf'({basename})\.(jpg|jpeg|png)', rf'\1.webp', new_content, flags=re.IGNORECASE
        )
        file_replace += n
    if new_content != content:
        with open(path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"  → {file_replace} 箇所置換")
        replace_count += file_replace

print(f"全置換完了: {replace_count} 箇所")
