#-*-coding：UTF-8 -*-
###Vivian
import os
import csv


#File process function: Union all the csv files scraped from the website
# 北京
# ./sj/北京迁入人数.csv
# 广州
# ./sj/广州迁入人数.csv
def get_filelist(dir):
    result = []
    for home, dirs, files in os.walk(dir):
        #print("#######file list#######")
        for filename in files:
            if filename.endswith('迁入人数.csv'):
                cityname = filename.strip('迁入人数.csv')
                fullname = os.path.join(home, filename)
                # print(fullname)
                ele = (cityname, fullname)
                result.append(ele)
    return result
#去最后lastnumber个元素,从csv文件读
def getsumoflast(filepath,lastnumber = 15):
    result = []
    f = csv.reader(open(filepath, 'r'))
    for i in f:
        result.append(i)
    lastNumberList = result[-1*lastnumber:]
    sum= 0.0
    for i in lastNumberList:
        sum = sum + float(i[1])#读出来的第二行是str。需要转成float
    return str(sum)
#写入一个csv文件
def write_csv(data, filename):
    with open(filename, "w",encoding='utf-8-sig') as f:#w的意思 https://zhidao.baidu.com/question/1637716327855830940.html
        f_csv = csv.writer(f)
        #一行一行写入
        f_csv.writerows(data)


if __name__ == "__main__":
    citys = get_filelist('./sj')
    writeCsvList = []
    writeCsvList.append(['城市名称','数据汇总'])#头文件
    for cityname,cityfilepath in citys:#遍历所有的文件i，cityname，j，cityfilepath
        rs = getsumoflast(cityfilepath)
        ele = [cityname,rs]
        writeCsvList.append(ele)
    write_csv(writeCsvList,'./result.csv')
