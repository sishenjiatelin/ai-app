import requests
import logging
import time
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
    # url = "https://httpbin.org/post"
    url = "https://httpbin.org/status/500"
    success = False
    for i in range(3):
        try:
            response = requests.post(url,data={"content":text},timeout=5)
            response.raise_for_status()
            print("第", i + 1, "次请求成功")
            logging.info(f"第 {i + 1} 次请求成功，输出：{response.text}")
            success = True
            break
        except Exception as e:
            print("第", i + 1, "次请求失败：", e)
            logging.error(f"第 {i + 1} 次请求失败：{e}")
            time.sleep(1)
    if not success:
        logging.error("请求失败：已经重试 3 次，程序结束")
except Exception as e:
    print("程序出错了：", e)
    logging.error(f"错误：{e}")