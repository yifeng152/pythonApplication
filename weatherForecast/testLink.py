import urllib.request
from city import city
import json

exit=False

while not exit:
    cityname=input("你想查询哪个城市的天气？输入q退出\n")
    if cityname=="q" or cityname=="Q":
        print("退出！")
        exit=True
    else:
        citycode=city.get(cityname)
        if citycode:
            url=("http://www.weather.com.cn/data/cityinfo/%s.html"%citycode)
            request=urllib.request.Request(url)
            response=urllib.request.urlopen(request)
            content=response.read().decode("utf-8")
            str1_json = json.loads(content)
            #print(type(str1_json))
            print ('更新时间:',end=' ')
            print(str1_json['weatherinfo']['ptime'])            
            print ('城    市:',end=' ')
            print(str1_json['weatherinfo']['city'])
            print ('天    气:',end=' ')
            print(str1_json['weatherinfo']['weather'])            
            print ('最高温度:',end=' ')
            print(str1_json['weatherinfo']['temp1'])
            print ('最低温度:',end=' ')
            print(str1_json['weatherinfo']['temp2'])                        

            #print(content)
