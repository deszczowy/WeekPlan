class Reader:
    def __init__(self, file_path, logger):
        self.file = file_path
        self.logger = logger
        self.lines = []
        
    def get(self, data) -> bool:
        done = self.read()
        if done:
            self.clean_up()
            data.extend(self.lines)
        else:
            data = []
        return done
    
    def clean_up(self) -> None:
        lines = []
        for line in self.lines:
            if line == "":
                continue
            if line.startswith("#"):
                continue
            lines.append(line)
        self.lines = lines
    
    def read(self) -> bool:
        self.lines = []
        try:    
            with open(self.file, "r", encoding="utf-8") as file:
                self.lines = [line.strip() for line in file]
            return True
        except Exception as e:
            self.logger.notice("Error ocured while reading file: {0}".format(e))
            return False

        