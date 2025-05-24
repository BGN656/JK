import os
import shutil
from datetime import datetime

def backup_files(source_dir, backup_dir):
    """Копирует файлы из исходной директории в директорию резервного копирования."""
    if not os.path.exists(source_dir):
        print(f"Исходная директория '{source_dir}' не найдена.")
        return

    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)

    backup_subdir = os.path.join(backup_dir, datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))
    os.makedirs(backup_subdir)

    for root, _, files in os.walk(source_dir):
        for file in files:
            src_file = os.path.join(root, file)
            rel_path = os.path.relpath(src_file, source_dir)
            dest_file = os.path.join(backup_subdir, rel_path)

            os.makedirs(os.path.dirname(dest_file), exist_ok=True)
            shutil.copy2(src_file, dest_file)

    print(f"Резервное копирование завершено. Файлы сохранены в '{backup_subdir}'.")

if __name__ == "__main__":
    print("Автоматизация резервного копирования")
    source_dir = input("Введите путь к исходной директории: ").strip()
    backup_dir = input("Введите путь к директории резервного копирования: ").strip()

    backup_files(source_dir, backup_dir)