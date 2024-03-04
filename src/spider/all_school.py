import pandas as pd
from include.method1 import *
from include.preprocessing import *

"""
基本思路：
    1 解析出大学的/university/PKU部分
    2 拼接出获取各大学信息的url
    3 解析response，获取学校信息
    4 重点获取schoolid，后续爬课需要
"""
# 第一步：获取各学校的/university/PKU

base_school_url = "https://www.icourse163.org/university/view/all.htm"
headers = get_headers()
print(get_response(url=base_school_url,headers=headers).text)
base_school_page = etree.HTML(get_response(url=base_school_url,headers=headers).text)
# /university/PKU部分 对应的中文校名
print(base_school_page)
part_school_url = base_school_page.xpath('/html/text()')
print(part_school_url)
# school_name_cn = base_school_page.xpath('/html/body/div[4]/div[2]/div/div[2]/div[2]/a/img/@alt')
# print(school_name_cn)
# # 第二步：拼接出获取各学校信息的链接
# school_url_list = []
# for part_url in part_school_url:
#     school_url_list.append("https://www.icourse163.org/"+part_url)
#
# # 第三步：访问各个学校的链接，得到详细信息，关键是schoolid,顺便封装数据
# df = pd.DataFrame(columns=['id', 'school_name', 'sort_name', 'comment'])
# for url in school_url_list:
#     sc_page = get_response(url=url,headers=headers).text
#     sc_page_tree = etree.HTML(sc_page)
#     # ()捕获数字schoolid
#     schoolId = re.findall(r'schoolId = "(\d+)"', sc_page)[0]
#     # 学校中文名称
#     schoolName = sc_page_tree.xpath('/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div/h1/text()')[0]
#     # 学校简介
#     schoolText = sc_page_tree.xpath('/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div/p/text()')[0]
#     # 学校英文简称
#     schoolNameEn = get_sort_name(school_name_cn,part_school_url,schoolName)
#
#     print(schoolId,schoolName,schoolNameEn,schoolText)
#
#     # 存入dateframe
#     df.loc[len(df)] = [schoolId,schoolName,schoolNameEn,schoolText]
#
# print(df)
# # 第四步：预处理，提取985、211标签
# # school_data_preprocessing(df)
# #
# # df.to_csv("../../data/all_school.csv",index=False)




