import urllib.request


result = 'city = {\n'

url1 = 'http://m.weather.com.cn/data5/city.xml'
request=urllib.request.Request(url1)
response=urllib.request.urlopen(request)
content=response.read().decode("utf-8")
provinces = content.split(',')
print(type(provinces))
print(provinces)




url = 'http://m.weather.com.cn/data3/city%s.xml'
for p in provinces:
    p_code = p.split('|')[0]
    url2 = url % p_code
    requestPro2=urllib.request.Request(url2)
    responsePro2=urllib.request.urlopen(requestPro2)
    contentPro2=responsePro2.read().decode("utf-8")
    cities = contentPro2.split(',')
    print(cities)


    #cities中存储的是各个省份的市级城市
    for c in cities:
        c_code = c.split('|')[0]
        url3 = url % c_code
        request3=urllib.request.Request(url3)
        response3=urllib.request.urlopen(request3)
        content3=response3.read().decode("utf-8")
        districts = content3.split(',')
        print(districts)


        #districts存储的是县级城市
        #该地址已经是最细分地区，进一步使用url请求，是为了获取code
        for d in districts:
            # print(type(d))
            d_pair = d.split('|')
            d_code = d_pair[0]
            name = d_pair[1]
            # print(d_code)
            if d_code == '06039':
                continue   
            url4 = url % d_code
            request4=urllib.request.Request(url4)
            response4=urllib.request.urlopen(request4)
            content4=response4.read().decode("utf-8")
            print(content4)
            code = content4.split('|')[1]
            line = "    '%s': '%s',\n" % (name, code)
            result = result+line
            # print(line)
            # print(code)

    print("----End of Province",p.split('|')[1])

result += '}'
f = open('.\cityTest.py', 'w')
f.write(result)
f.close()
# print(result)



# content1 = urllib2.urlopen(url1).read()
# provinces = content1.split(',')



# url=("http://www.weather.com.cn/data/cityinfo/%s.html"%citycode)
# request=urllib.request.Request(url)
# response=urllib.request.urlopen(request)
# content=response.read().decode("utf-8")
# print(content)