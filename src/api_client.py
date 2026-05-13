import requests
import logging
import time

class ApiClient:
    def __init__(self, url: str, timeout: int = 5, retry_times: int = 3):
        self.url = url
        self.timeout = timeout
        self.retry_times = retry_times
    

    def post_text(self, text: str) -> str | None:
        for i in range(self.retry_times):
            try:
                response = requests.post(
                    self.url,
                    data={"content": text},
                    timeout=self.timeout
                )

                response.raise_for_status()

                data = response.json()
                content = data["form"]["content"]

                logging.info(f"第 {i + 1} 次请求成功")
                return content

            except Exception as e:
                logging.error(f"第 {i + 1} 次请求失败: {e}")
                time.sleep(1)

        logging.error("所有请求都失败")
        return None
