# encoding:utf-8

import os
import sys
import pandas as pd

'''设置主项目目录，在cmd下执行该脚本不会出现导入其他py文件发生错误'''
sys.path.append(r'D:\code\Python\pycharm-python\d_point\craw_project')
import warnings
warnings.filterwarnings('ignore')


from datetime import datetime, timedelta
from craw_NCP_info import init_selenium, craw_info
from preprocess_data import process_data, save_to_mysql, compare_data, rename_df

# 显示所有列
pd.set_option('display.max_columns', None)
# 显示所有行
# pd.set_option('display.max_rows', None)

if __name__ == '__main__':
    
    # 设置昨天的日期作为数据日期
    data_time = datetime.now() + timedelta(-1)
    data_time_str = data_time.strftime('%Y-%m-%d')
    print('程序开始，正在爬取最新疫情数据...')

    """爬虫获取数据"""
    # 丁香园网站
    url = 'https://ncov.dxy.cn/ncovh5/view/pneumonia'
    # ①初始化 selenium
    browser = init_selenium()
    # ②获取城市和省份的数据
    df_city_data, df_province_data = craw_info(browser, url)

df_city_data["date"]=data_time_str
df_province_data["date"]=data_time_str

df_province_data.to_excel("/Users/macbook/Desktop/ncv_real_time.xlsx")



import pandas as pd
from pandasql import sqldf
pysqldf = lambda sql: sqldf(sql, globals())



df_target=pysqldf("""
                     select "city" as "城市","date"as"日期","curr_diagnose" as"现存确诊", "sum_diagnose" as "累计确诊","death" as "死亡","cure" as "治愈"
                     from df_city_data 
                     where "city" in ("东莞","成都","佛山","长沙","苏州","昆明","南京","重庆","惠州","厦门","沈阳","广州","深圳")
                     union all
                     select "province"as "城市","date"as"日期","curr_diagnose" as"现存确诊", "sum_diagnose" as "累计确诊","death" as "死亡","cure" as "治愈"
                     from df_province_data 
                      where "province" in ("北京","上海","深圳") """)

df_target.to_csv("/Users/macbook/Desktop/ncv_target.csv",encoding='utf_8_sig')
print('数据爬取完毕')
