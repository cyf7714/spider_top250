#思路
#1.拿到页面源代码
#2.编写正则,提取页面数据
#3.保存数据
import rspy 
import requests
f=open("top250.csv",mode='w',encoding='utf-8')
for i in range(0,250,25):
  url=f"https://movie.douban.com/top250?start={i}&filter="
  headers={
    "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Mobile Safari/537.36 Edg/127.0.0.0"

  }
  resp=requests.get(url,headers=headers)
  #resp.encoding='utf-8' 解决乱码问题
  pageSource=resp.text
  # print(pageSource)
  #编写正则表达式
  #re.S 可以让正则中的.匹配换行符
  obj=re.compile(r'<div class="item">.*?<span class="title">(?P<name>.*?)</sp'
                 r'an>.*?<p class="">.*?导演: (?P<daoyan>.*?)&nbsp;.*?<br>'
                 r'(?P<year>.*?)&nbsp;.*?<span class="rating_num" property="v:average">'
                 r'(?P<rating>.*?)</span>.*?<span>(?P<num>.*?)人评价</span>',re.S)

  #进行正则匹配
  res=obj.finditer(pageSource)
  for item in res:
      name=item.group('name')
      daoyan=item.group('daoyan')
      year=item.group('year').strip()
      rating=item.group('rating')
      num=item.group('num')
      f.write(f"{name},{daoyan},{year},{rating},{num}\n")
f.close()
resp.close()


