import json
import time

from include.method1 import *

"""
https://www.icourse163.org/web/j/mocSearchBean.searchCourseCardByChannelAndCategoryId.rpc?csrfKey=658b7b32976b43ba8e3e4f0ea563aaf2
 - 求职就业、期末突击、专升本、四六级、期末资料
 - 6001、4003、44001、48001、79002

基本思路：
    1 获取各类别的channel_id,需要referer
    2 改变post请求体的channel_id、page部分获取新的请求数据
    3 根据首次访问的页面数确定循环次数

"""

url = "https://www.icourse163.org/web/j/courseBean.getCourseListBySchoolId.rpc?csrfKey=658b7b32976b43ba8e3e4f0ea563aaf2"


# 步骤一：获取channel_id列表
channel_id_list = [6001,4003,44001,48001,79002]
referer_list = ["https://www.icourse163.org/channel/6001.htm",
                "https://www.icourse163.org/channel/4003.htm",
                "https://www.icourse163.org/channel/44001.htm?cate=-1&subCate=-1",
                "https://www.icourse163.org/channel/48001.htm?cate=-1&subCate=-1",
                "https://www.icourse163.org/channel/79002.htm"]

# 步骤二：先获取最大课程数量，在针对不同channel、不同页面定制data部分
# columns=['id','course_name','teacher_name','course_original_price','course_sale_price','course_sale_num','deleted']

all_external_course_list = []
for i in range(len(channel_id_list)-2):
    # 首次访问该channel的课程页面
    data = get_channel_post_data(channel_id_list[i], 1)

    # 需要添加referer的请求头
    print(data)
    headers = get_headers(referer=referer_list[i])
    print(headers)
    first_resp_json = get_response(url=url, headers=headers, data=data).json()
    # 最大页数
    print(first_resp_json)
    time.sleep(10)
    max_page = first_resp_json['result']['query']['totlePageCount']
    # 首页信息爬取
#     if first_resp_json['result']['list']:
#         external_course_json_to_list(first_resp_json,all_external_course_list)
#         print(f"【{channel_id}】的《1/{max_page}》页爬取成功")
#
#     # 其他页信息爬取
#     for page in range(2, max_page + 1):
#         data = get_channel_post_data(channel_id, page)
#         resp_json = get_response(url=url, headers=headers, data=data).json()
#         if resp_json['result']['list']:
#             # 信息提取到all_course_list
#             external_course_json_to_list(resp_json, all_external_course_list)
#             print(f"【{channel_id}】的《{page}/{max_page}》页爬取成功")
#         else:
#             print(f"【{channel_id}】的《{page}/{max_page}》页爬取失败")
#
# # 创建结果dataframe
# columns=['id','course_name','teacher_name','course_original_price','course_sale_price','course_sale_num','deleted']
# df = pd.DataFrame(all_external_course_list, columns=columns)
# df.to_csv("../../data/all_external_course.csv", index=False)