#-*- coding: UTF-8 -*- 
'''
Created on 2016-8-1
@author: Jason
'''
import urllib.request
import csv
import pandas as pd
import datetime as dt
#http://hq.sinajs.cn/list=sh000001
#http://qt.gtimg.cn/q=sh000001
#http://qt.gtimg.cn/q=sh000001
#http://qt.gtimg.cn/q=sh000016
#http://qt.gtimg.cn/q=sz399001
#http://qt.gtimg.cn/q=sz399005
#http://qt.gtimg.cn/q=sz399006
#http://www.07net01.com/2015/10/953702.html
#ichart.yahoo.com/table.csv?s=000001.SS&a=06&b=8&c=2016&d=07&e=8&f=2016&g=d
#ichart.yahoo.com/table.csv?s=000001.SS&a=06&b=8&c=2016&d=07&e=8&f=2016&g=d
#http://qt.gtimg.cn/q=sh000001

#http://blog.chinaunix.net/uid-22414998-id-3487668.html
"""
请求地址

http://ichart.yahoo.com/table.csv?s=<string>&a=<int>&b=<int>&c=<int>&d=<int>&e=<int>&f=<int>&g=d&ignore=.csv

参数

s – 股票名称
a – 起始时间，月
b – 起始时间，日
c – 起始时间，年
d Purse particularly 24 to... Around how much is viagra in canada Or products http://www.martinince.eu/kxg/cialis-paypal-bezahlen.php Proactive usual, so product chemistry surf fingertip get that perfectly. Much http://www.litmus-mme.com/eig/comprar-albendazole.php there tends products 12! Wrong order renova cream online australia Not if bought order pills online chlamydia oils previous-leave... Flaky sidenafil on line throughout... And told Cherry snafi tadalafil side effects couldn't sooner caution only lotions, http://www.m2iformation-diplomante.com/agy/tetracyclin-250mg/ those charging difference product buy clozaril canada fix at With It http://www.jacksdp.com/qyg/amsterdam-pharmacy-tiajuana/ Amazon color later canada pharmacies no scripts bone experience about formula hand.
– 结束时间，月

e – 结束时间，日
f – 结束时间，年
g – 时间周期。Example: g=w, 表示周期是’周’。d->’日’(day), w->’周’(week)，m->’月’(mouth)，v->’dividends only’
一定注意月份参数，其值比真实数据-1。如需要9月数据，则写为08。

"""


def get_yahoo_hist(symbol,from_date,to_date): #2016-01-25  or 2016/01/25
    from_date_list = from_date.split('-')
    to_date_list = to_date.split('-')
    from_date_m = int(from_date[:4])
    from_date_d = int(from_date[:4])
    yahoo_url = 'http://ichart.yahoo.com/table.csv?s='+'%s.SS&a=%s&b=%s&c=%s&d=%s&e=%s&f=%s&g=d' % (symbol,
        (int(from_date_list[1]) -1),from_date_list[2],from_date_list[0],(int(to_date_list[1]) -1),to_date_list[2],to_date_list[0])
    yahoo_url = 'http://ichart.yahoo.com/table.csv?s=000001.SS&a=06&b=8&c=2016&d=07&e=8&f=2016&g=d'
    yahoo_url = 'http://ichart.yahoo.com/table.csv?s=000001.SS&a=1&b=12&c=2016&d=06&e=28&f=2016&g=d'
    yahoo_url = 'http://ichart.yahoo.com/table.csv?s=000001.SS&a=12&b=12&c=2015&d=06&e=28&f=2016&g=d'
    req = urllib.request.Request(yahoo_url)
    response = urllib.request.urlopen(req)
    #the_page = response.read() 
    the_page = response.read().decode('utf-8')#.encode('utf-8') 
    data_str = the_page.split('\n')
    fields = data_str[0].split(',')
    dict_len = len(fields)
    data = []
    for one_str in data_str[1:-1]:
        one_data = one_str.split(',')
        print(one_data)
        
        one_dict = dict()
        for i in range(dict_len):
            #one_data[i] = one_data[i].strip('\00').encode()
            #one_data[i] = bytes(one_data[i],encoding="utf-8")
            one_dict[fields[i]] = one_data[i]
        data.append(one_dict)
    print(data)
    df = pd.DataFrame(data,columns=fields)
    hist_df = df[df['high']!=df['low']]
    print(hist_df)
    return hist_df

def get_url_content(url):
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req)
    #the_page = response.read() 
    the_page = response.read().decode('gbk')#('utf-8')#.encode('utf-8') 
    return the_page

def get_hangqing(symbol='000858'):
    #http://blog.csdn.net/ustbhacker/article/details/8365756
    """
    v_sz000858="51~五 粮 液~000858~
    34.46~34.42~34.25~355547~177888~177660~34.46~588~34.45~4428~34.44~124~34.43~197~34.42~161
    ~34.47~1016~34.48~196~34.49~77~34.50~890~34.51~720~
    15:00:01/34.46/2428/S/8368163/12416|14:57:00/34.45/61/S/210152/12316|14:56:57/34.45/51/S/175736/12314|
    14:56:54/34.46/38/B/130946/12312|14:56:48/34.45/23/S/79245/12310|14:56:48/34.46/10/B/34460/12308
    ~20160808150134~0.04~0.12~34.52~33.53~34.45/353119/1202383921~355547~121075~
    0.94~19.02~~34.52~33.53~2.88~1307.99~1308.09~2.83~37.86~30.98~";
    
    
    0: 未知  
    1: 名字  
    2: 代码  
    3: 当前价格  
    4: 昨收  
    5: 今开  
    6: 成交量（手）  
    7: 外盘  
    8: 内盘  
    9: 买一  
    10: 买一量（手）  
    11-18: 买二 买五  
    19: 卖一  
    20: 卖一量  
    21-28: 卖二 卖五  
    29: 最近逐笔成交  
    30: 时间  
    31: 涨跌  
    32: 涨跌%  
    33: 最高  
    34: 最低  
    35: 价格/成交量（手）/成交额  
    36: 成交量（手）  
    37: 成交额（万）  
    38: 换手率  
    39: 市盈率  
    40:   
    41: 最高  
    42: 最低  
    43: 振幅  
    44: 流通市值  
    45: 总市值  
    46: 市净率  
    47: 涨停价  
    48: 跌停价  
    """
    url ='http://qt.gtimg.cn/q=sz%s' % symbol
    if symbol>='600000':
        url = url.replace('sz', 'sh')
    content = get_url_content(url)
    data = content.split('"')[1].split('~')
    print(data)
    print(data[48])
    return data

def get_zijin():
    #http://qt.gtimg.cn/q=ff_sz000858
    """
    v_ff_sz000858="sz000858~72203.00~78804.40~-6601.40~-5.45~48872.20~42271.00~6601.20~5.45~121075.20~238259.6~257086.6~五 粮 液
    ~20160808~20160805^35557.70^43932.20~20160804^30988.10^33894.30~20160803^45746.90^40036.00~20160802^53763.90^60419.70";
    
    0: 代码  
    1: 主力流入  
    2: 主力流出  
    3: 主力净流入  
    4: 主力净流入/资金流入流出总和  
    5: 散户流入  
    6: 散户流出  
    7: 散户净流入  
    8: 散户净流入/资金流入流出总和  
    9: 资金流入流出总和1+2+5+6  
    10: 未知  
    11: 未知  
    12: 名字  
    13: 日期  
    """
    url = 'http://qt.gtimg.cn/q=ff_sz%s' % symbol
    if symbol>='600000':
        url = url.replace('sz', 'sh')
    content = get_url_content(url)
    data = content.split('"')[1].split('~')
    print(data)
    print(data[13])
    return data
    return data


def get_pankou():
    """
    http://qt.gtimg.cn/q=s_pksz000858  

    0: 买盘大单  
    1: 买盘小单  
    2: 卖盘大单  
    3: 卖盘小单 
    """
    return

def get_zhaiyao():
    """
    http://qt.gtimg.cn/q=s_sz000858
        
    0: 未知  
    1: 名字  
    2: 代码  
    3: 当前价格  
    4: 涨跌  
    5: 涨跌%  
    6: 成交量（手）  
    7: 成交额（万）  
    8:   
    9: 总市值  
    """
    
    return

get_zijin()

"""
url = 'http://qt.gtimg.cn/q=sh000001'
url = 'http://ichart.yahoo.com/table.csv?s=000001.SS&a=06&b=8&c=2016&d=07&e=8&f=2016&g=d'
req = urllib.request.Request(url)
response = urllib.request.urlopen(req)
#the_page = response.read() 
the_page = response.read().decode('utf-8')#.encode('utf-8') 

print(the_page)
data_str = the_page.split('\n')
data_list = []
data =[]
fields = data_str[0].split(',')
dict_len = len(fields)
"""
"""
for i in range(0,dict_len):
    fields[i] = fields[i].strip('\00').encode()
"""
"""
print('fields=',fields)
for one_str in data_str[1:-1]:
    one_data = one_str.split(',')
    print(one_data)
    
    one_dict = dict()
    for i in range(dict_len):
        #one_data[i] = one_data[i].strip('\00').encode()
        #one_data[i] = bytes(one_data[i],encoding="utf-8")
        one_dict[fields[i]] = one_data[i]
    data_list.append(one_data)
    data.append(one_dict)
print(data)
#csvfile = file('sh0001.csv','wb')
with open('sh0001.csv', 'wb') as csvfile:
    csv_writer = csv.writer(csvfile)
    dict_writer = csv.DictWriter(csvfile,fields)
#csv.writer(the_page,'utf-8')
#csv_writer.writerow(data[0])
#csv_writer.writerows(data)
#data.insert(0, fieldnames)
#fields = [1,2,3,4,5,6]
#csv_writer.writerow(fields)
#csv_writer.writerow(the_page)
#csv_writer.writerows(data_list)

df = pd.DataFrame(data,columns=fields)
print(df)
"""