import requests
url = 'https://daily.zhihu.com'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
res =requests.get(url,headers=headers).text
print(res)