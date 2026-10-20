class Tool:

    @staticmethod
    def change_extension(file_path: str, new_extension: str) -> str:
        """Changing extension in given file name. Method will add extension if file name do not have one."""

        from pathlib import Path
        path = Path(file_path)
        new_extension = new_extension.lstrip(".")
        new_path = path.with_suffix(f".{new_extension}")
        return str(new_path)