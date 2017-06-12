import requests

cookies = {}
raw_cookies = 'll="108288"; bid=gwGeinNd2I4; _pk_id.100001.8cb4=5374692107313e19.1496297786.2.1496908333.1496298423.; __utma=30149280.2132437356.1496297788.1496297788.1496908321.2; __utmz=30149280.1496297788.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); ps=y; ue="longzitan@126.com"; push_noty_num=0; push_doumail_num=0; __utmv=30149280.5278; __yadk_uid=PoOEbkJSzLH1pHp4VZdHdEzupFIsV75P; _ga=GA1.2.2132437356.1496297788; _vwo_uuid_v2=A4F1ECECF52B44E9F47321A20A127980|add0f93b06cb79bf5351f7b4f720e023; _pk_ses.100001.8cb4=*; __utmb=30149280.3.10.1496908321; __utmc=30149280; __utmt=1; dbcl2="52781462:+B2wEJ/yWEk"; ck=kjSH'

for line in raw_cookies.split(';'):
    key,value = line.split('=',1)
    cookies[key]=value
print cookies
test = "https://www.douban.com/group/"
req = requests.get(test,cookies=cookies)
print req.text
