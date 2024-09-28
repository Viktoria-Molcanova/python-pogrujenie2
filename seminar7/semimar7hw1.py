from pathlib import Path

__all__ = ['rename']

def rename(new_name: str, ext_renamed: str, /, count_dig: int = 3, ext_new: str = None,
                       saved_range: range = (3, 6), path: str = None) -> int:
    ext_new = ext_new or ext_renamed
    work_path = Path.cwd() if path is None else Path(path)
    files_to_rename = [p for p in work_path.glob(f"*{ext_renamed}")]

    for count_renamed, p in enumerate(files_to_rename):
        file_name = f"{p.stem[saved_range[0]:saved_range[1]]}{new_name}{count_renamed:03}{ext_new}"
        p.rename(p.parent / file_name)

    return len(files_to_rename)

if __name__ == '__main__':
    rename("book", ".txt")
