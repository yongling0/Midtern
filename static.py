import requests
from bs4 import BeautifulSoup
import pandas as pd

# 目標網址
url = "https://airtw.moenv.gov.tw/CHT/Information/Standard/AirQualityIndicator.aspx"
headers = {"User-Agent": "Mozilla/5.0"}
res = requests.get(url, headers=headers)
res.encoding = "utf-8"

# 解析 HTML
soup = BeautifulSoup(res.text, "html.parser")

# 找出正確的表格
tables = soup.find_all("table")
target_table = None
for table in tables:
    if "空氣品質指標 AQI" in table.text:
        target_table = table
        break

if not target_table:
    print("❌ 找不到目標表格")
    exit()

# 擷取表格所有行
rows = target_table.find_all("tr")
data = []

# 第一行是 AQI 等級欄位（第一個 th 是空的）
headers = [th.get_text(strip=True) for th in rows[0].find_all("th")]
# headers[0] 是空字串，可以改為 “項目”
headers[0] = "項目"

# 擷取每列資料
for row in rows[1:]:
    cells = row.find_all(["th", "td"])
    row_data = [cell.get_text(strip=True) for cell in cells]
    data.append(row_data)

# 建立 DataFrame
df = pd.DataFrame(data, columns=headers)
df.to_csv("static.csv", index=False, encoding="utf-8-sig")
print("✅ 表格已儲存為 static.csv")
