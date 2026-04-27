import requests
import logging
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR/ "data" / "input.txt"
LOG_FILE = BASE_DIR/ "logs" / "log.txt"
logging.basicConfig(filename = LOG_FILE,level = logging.INFO,
format = "%(asctime)s | %(levelname)s |%(message)s",encoding="utf-8")
try:
    with open(DATA_DIR,"r",encoding="utf-8")as f:
        text = f.read()
    print("内容：",text)
    logging.info(f"输入：{text}")
    url = "https://httpbin.org/post"
    response = requests.post(url,data={"content":text},timeout=5)
    response.raise_for_status()
    print("服务器回给我的是：", response.text)
    logging.info(f"输出：{response.text}")
except Exception as e:
    print("程序出错了：", e)
    logging.error(f"错误：{e}")