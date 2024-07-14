import os


def extract_file_details(file_path):
    try:
        path, full_name = os.path.split(file_path)
        name, extension = os.path.splitext(full_name)
        return path, name, extension
    except Exception as e:
        print(f"Ошибка: {e}")
        return None, None, None

file_path = "C:/Users/Public/Desktop/IntelliJ IDEA Ultimate 2024.1.lnk"
path, name, extension = extract_file_details(file_path)
print("Path:", path)
print("Name:", name)
print("Extension:", extension)
