import requests
import logging
import time
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR/ "data" / "input.txt"
LOG_FILE = BASE_DIR/ "logs" / "log.txt"
url_post = "https://httpbin.org/post"
url_test = "https://httpbin.org/status/500"
logging.basicConfig(filename = LOG_FILE,level = logging.INFO,
format = "%(asctime)s | %(levelname)s |%(message)s",encoding="utf-8")

def LogConfig():
    logging.basicConfig(filename = LOG_FILE,level = logging.INFO,
    format = "%(asctime)s | %(levelname)s | %(message)s",
    encoding = "utf-8")

def READ_Text():
    with open(DATA_DIR,"r",encoding = "utf-8")as f:
        text = f.read()
    print("内容：",text)
    logging.info(f"输入：{text}")
    return text

def Call_API(url,text):
    for i in range(3):
        try:
            respose = request.post(url,data = {"content":text},timeout = 5)
            respose.raise_for_status()
            data = respose.json()
            content = data["form"]["content"]
            print(f"第{i+1}次失败")
            logging.info(f"第{i+1}次成功,输出{content}")
            return content
        except Exception as e:
            logging.error(f"第{i+1}次请求失败：{e}")
            time.sleep(1)
    logging.error(f"第三次失败,请求失败！")
    return None
    
def main():
    try:
        LogConfig()

        text = READ_Text()
        content = Call_API(url_test,text)

        if content is None:
            print("请求失败，请查看日志")
        else:
            print("接口收到的内容是：", content)

    except Exception as e:
        print("程序出错了：", e)
        logging.error(f"程序失败：{e}")


if __name__ == "__main__":
    main()