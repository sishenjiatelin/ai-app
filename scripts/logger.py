import requests
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR/ "data" / "input.txt"
LOG_DIR = BASE_DIR/ "logs" / "log.txt"
with open(DATA_DIR,"r",encoding="utf-8")as f:
    text = f.read()
print("内容：",text)
url = "https://httpbin.org/post"
response = requests.post(url,data={"content":text})
print("服务器回给我的是：", response.text)
with open(LOG_DIR,"a",encoding="utf-8")as f:
    f.write("输入："+ "\n" + text+ "\n")
    f.write("输出：" +  "\n" + response.text + "\n")