import datetime
import time

from include.method1 import *
"""
https://www.icourse163.org/web/j/mocCourseV2RpcBean.getCourseEvaluatePaginationByCourseIdOrTermId.rpc?csrfKey=658b7b32976b43ba8e3e4f0ea563aaf2

基本思路：
    1 获取所有的course_id
    2 改变post请求体的courseId、page部分获取新的请求数据
    3 根据首次访问的页面数确定循环次数

"""
url = 'https://www.icourse163.org/web/j/mocCourseV2RpcBean.getCourseEvaluatePaginationByCourseIdOrTermId.rpc?csrfKey=fcb924b33b7342548d079a5b312ddb29'
headers = get_comment_headers("")

# 步骤一：获取所有course_id
course_id_list = get_course_id()

# 步骤二：获取评论页数，在针对不同课程、不同页面定制data部分
starttime = datetime.datetime.now()
all_comment_list = []
for course_id in course_id_list:
    # 首次访问
    data = get_comment_post_data(course_id,1)
    first_resp_json = get_response(url=url, headers=headers, data=data).json()
    # 最大页数
    max_page = first_resp_json['result']['query']['totlePageCount']
    print(first_resp_json)
    # 首页信息获取
    if first_resp_json['result']['list']:
        comment_json_to_list(first_resp_json,course_id,all_comment_list)
        print(f"【{course_id}】的《1/{max_page}》页爬取成功")

    # 其他页信息爬取
    for page in range(2, max_page + 1):
        data = get_comment_post_data(course_id, page)
        resp_json = get_response(url=url, headers=headers, data=data).json()
        if resp_json['result']['list']:
            # 信息提取到all_course_list
            comment_json_to_list(resp_json, course_id,all_comment_list)
            print(f"【{course_id}】的《{page}/{max_page}》页爬取成功")
        else:
            print(f"【{course_id}】的《{page}/{max_page}》页爬取失败")

endtime = datetime.datetime.now()
print (f"爬取时间：{endtime - starttime}")

# 创建结果dataframe
print(all_comment_list[0])
# 评论id，评论者id，评论课程id，评论者昵称，评论内容，用户评分，点赞数
columns = ['id','commentor_id','course_id','user_nick_name','content','mark','agreeCount']
df = pd.DataFrame(all_comment_list, columns=columns)
df.to_csv("../../data/all_course_comment.csv",index=False)
