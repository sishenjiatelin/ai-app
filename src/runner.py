from src.file_reader import *
from src.api_client import *
from src.config import *
import logging

def setup_logging():
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)

    logging.basicConfig(
        filename=LOG_FILE,
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
        encoding="utf-8"
    )


def run():
    setup_logging()

    try:
        reader = TextFileReader(DATA_FILE)
        text = reader.read()

        client = ApiClient(
            url=API_URL,
            timeout=TIMEOUT,
            retry_times=RETRY_TIMES
        )

        content = client.post_text(text)

        if content is None:
            print("请求失败，请查看日志")
        else:
            print("接口收到的内容是：", content)

    except Exception as e:
        print("程序出错了：", e)
        logging.error(f"程序失败: {e}")
