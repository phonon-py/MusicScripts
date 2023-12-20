import os

def confirm_deletion(file_path):
    response = input(f"本当に '{file_path}' を削除してもよろしいですか？ [y/N]: ")
    return response.lower() == 'y'

# 削除する特定のファイル名
file_name_to_delete = '地元の歌_136_G#min.mp3'

# 削除対象のディレクトリ
target_folders = [
    '/Users/kimuratoshiyuki/Dropbox/DEMO＿ALL_update',
    '/Users/kimuratoshiyuki/Dropbox/DEMO＿ALL_Authority'
]

# 各ターゲットフォルダに対して
for folder in target_folders:
    file_path = os.path.join(folder, file_name_to_delete)
    # ファイルが存在する場合は削除の確認を求める
    if os.path.exists(file_path):
        if confirm_deletion(file_path):
            os.remove(file_path)
            print(f"Deleted: {file_path}")
        else:
            print(f"Skipped: {file_path}")
    else:
        print(f"File not found: {file_path}")