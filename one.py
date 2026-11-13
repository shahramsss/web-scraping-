import requests
from bs4 import BeautifulSoup
import re

url = "https://divar.ir/s/iran/computer-parts-accessories?sort=sort_date"


response = requests.get(url)

# print(response)
# print(response.url)
# print(response.status_code)
# print(response.request.headers)
# print(response.request)
# print(response.reason)
# print(response.text)

content = BeautifulSoup(response.text, "html.parser")
# print(content.find('h2'))
# print(content.findAll('h2'))
# print(content.find_all('h2'))
# print(content.find_all(['h1' ,'h2']))
# print(content.find('h2').attrs)
# print(content.find('h2').text)
# print(content.find('h2').name)
# print(content.find(attrs={"id":"app"}))
# print(content.find(class_="kt-post-card__title"))
# print(content.find("div" , class_="kt-post-card__title"))
# print(len(content.find_all("h2" )))
# print(len(content.find_all("h2" , limit=5)))
# print(content.find("div").get("id"))
# print(content.find(re.compile("^div")))
print(content.select('div[class=kt-post-card__body]'))
