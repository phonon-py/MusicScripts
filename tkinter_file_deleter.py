import os
import tkinter as tk
from tkinter import filedialog, messagebox

def delete_file(file_name, folders):
    for folder in folders:
        file_path = os.path.join(folder, file_name)
        if os.path.exists(file_path):
            # ユーザーに確認を求める
            response = messagebox.askyesno("Confirm Deletion", f"本当に削除してもいいですか？\n '{file_path}'?")
            if response:
                try:
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")
                except Exception as e:
                    print(f"Error deleting {file_path}: {e}")
            else:
                print(f"Deletion cancelled: {file_path}")
        else:
            print(f"File not found: {file_path}")

def on_delete():
    file_name = entry_file_name.get()
    folder_paths = text_folders.get("1.0", tk.END).strip().split('\n')

    if not file_name or not folder_paths:
        messagebox.showerror("Error", "ファイル名と少なくとも1つのフォルダパスを入力してください。")
        return

    delete_file(file_name, folder_paths)
    messagebox.showinfo("Complete", "完了しました。")

app = tk.Tk()
app.title("File Deleter")

label_file_name = tk.Label(app, text="削除したいファイル名を拡張子も含め入力してください。(例:xxxx.xlsx):")
label_file_name.pack()

entry_file_name = tk.Entry(app)
entry_file_name.pack()

label_folders = tk.Label(app, text="削除対象のフォルダを一行に一つずつ入力してください:")
label_folders.pack()

text_folders = tk.Text(app, height=10)
text_folders.pack()

delete_button = tk.Button(app, text="Delete File", command=on_delete)
delete_button.pack()

app.mainloop()
