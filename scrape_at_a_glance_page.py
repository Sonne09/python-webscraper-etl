import requests
import re


cookies = {
    'ASP.NET_SessionId': 'n0a0dazanx4jeayvhg3pfmiw',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json; charset=UTF-8',
    # 'Cookie': 'ASP.NET_SessionId=n0a0dazanx4jeayvhg3pfmiw',
    'Origin': 'https://tis.nhai.gov.in',
    'Referer': 'https://tis.nhai.gov.in/tollplazasataglance.aspx?language=en',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
}

data = "{'TollName':''}"

response = requests.post(
    'https://tis.nhai.gov.in/TollPlazaService.asmx/GetTollPlazaInfoGrid',
    cookies=cookies,
    headers=headers,
    data=data,
)

# print(response.text)

list = re.findall('javascript:TollPlazaPopup\(\d+\)', response.text)
ids = [int(re.findall('\d+',str_)[0]) for str_ in list]
print(ids)
print(list)

