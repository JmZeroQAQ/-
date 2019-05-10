import requests
import re

url = input("请输入链接:")

fb = open('in.txt', 'w', encoding = 'utf-8')

response = requests.get(url)
response.encoding = 'utf-8'
html = response.text

content = re.findall(r'table class(.*?)/table', html, re.S)[0]
catch_list = re.findall(r'js-file-line">(.*?)</td>', content, re.S)

for catch in catch_list:
    cat_html = catch
    cat_html = '%s \n' % cat_html
    if(cat_html != ''):
        fb.write(cat_html)
    
print("已爬取完毕！")
