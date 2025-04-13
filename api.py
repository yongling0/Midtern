import requests
import csv

# 發送 GET 請求
url = 'https://bas.nccc.com.tw/nccc-nop/OpenAPI/D01/Fraud/IDSUM'
response = requests.get(url)
#print(response.text)


# 寫入檔案
with open("api.csv", "w", newline="", encoding="utf-8-sig") as f:
    f.write(response.text)

print("CSV 檔案已成功建立：api.csv")