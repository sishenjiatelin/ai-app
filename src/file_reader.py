import logging
from pathlib import Path

class TextFileReader:
    def __init__(self, file_path: Path):
        self.file_path = file_path

    def read(self) -> str:
        if not self.file_path.exists():
            raise FileNotFoundError(f"文件不存在: {self.file_path}")

        text = self.file_path.read_text(encoding="utf-8")
        logging.info(f"读取输入文件成功: {self.file_path}")

        return text