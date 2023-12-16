import os

def confirm_deletion(file_path):
    response = input(f"本当に '{file_path}' を削除してもよろしいですか？ [y/N]: ")
    return response.lower() == 'y'

# 削除するファイルがある元のフォルダ
source_folder = '/Users/kimuratoshiyuki/Dropbox/JB _Dora _Beats'

# 削除対象のフォルダ
target_folders = [
    '/Users/kimuratoshiyuki/Dropbox/DEMO＿ALL_update',
    '/Users/kimuratoshiyuki/Dropbox/DEMO＿ALL_Authority'
]

# 元のフォルダからファイル名を取得
files_to_delete = os.listdir(source_folder)

# 各ターゲットフォルダに対して
for folder in target_folders:
    # そのフォルダ内の各ファイルについて
    for file_name in files_to_delete:
        file_path = os.path.join(folder, file_name)
        # ファイルが存在する場合は削除の確認を求める
        if os.path.exists(file_path):
            if confirm_deletion(file_path):
                os.remove(file_path)
                print(f"Deleted: {file_path}")
            else:
                print(f"Skipped: {file_path}")
        else:
            print(f"File not found: {file_path}")
