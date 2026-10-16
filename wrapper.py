class Wrapper:

    def __init__(self, input_file, output_file) -> None:
        from schedule import Schedule
        from filereader import FileReader
        from plan import Plan

        output = output_file
        if output is None:
            output = self.change_extension(input_file, "png")

        shedule = Schedule()
        freader = FileReader(input_file, shedule)
        Plan(output, shedule)

    def change_extension(self, file_path: str, new_extension: str) -> str:
        from pathlib import Path
        
        path = Path(file_path)
        new_extension = new_extension.lstrip(".")
        new_path = path.with_suffix(f".{new_extension}")
        return str(new_path)