from include.method1 import *
import datetime
"""
https://www.icourse163.org/web/j/courseBean.getCourseListBySchoolId.rpc?csrfKey=2cb2d5f35fd945bca449588a64d96daa

基本思路：
    1 获取每个大学的课程数
    2 改变post请求体的school_id、page部分获取新的请求数据
    3 根据首次访问的页面数确定循环次数
    
    补充：
        可根据课程id进一步进入课程主页，获取课程属性、课程大纲、课程评论等
        https://www.icourse163.org/course/PKU-1461521170
"""


url = "https://www.icourse163.org/web/j/courseBean.getCourseListBySchoolId.rpc?csrfKey=970502919303499c805cb0a6ba7bfcf1"
headers = get_headers()

# 步骤一：获取school_id列表
school_id_list = get_school_id()

# 步骤二：先获取最大课程数量，在针对不同学校、不同页面定制data部分
# columns=['id','course_name','school_name','school_id','faculty_name','faculty_id','enroll_count','start_time','end_time','deleted']
starttime = datetime.datetime.now()
all_course_list = []
for school_id in school_id_list:
    # 首次访问该学校的课程页面
    data = get_post_data(school_id,1)
    first_resp_json = get_response(url=url,headers=headers,data=data).json()
    # 最大页数
    max_page = first_resp_json['result']['query']['totlePageCount']
    # 首页信息获取
    if first_resp_json['result']['list']:
        course_json_to_list(first_resp_json,all_course_list)
        print(f"【{school_id}】的《1/{max_page}》页爬取成功")

    # 其他页信息爬取
    for page in range(2,max_page+1):
        data = get_post_data(school_id,page)
        resp_json = get_response(url=url,headers=headers,data=data).json()
        if resp_json['result']['list']:
            # 信息提取到all_course_list
            course_json_to_list(resp_json,all_course_list)
            print(f"【{school_id}】的《{page}/{max_page}》页爬取成功")
        else:
            print(f"【{school_id}】的《{page}/{max_page}》页爬取失败")

endtime = datetime.datetime.now()
print (f"爬取时间：{endtime - starttime}")

# 创建结果dataframe
print(all_course_list[0])
columns = ['id','course_name','school_name','school_id','faculty_name','faculty_id','enroll_count','start_time','end_time','deleted']
df = pd.DataFrame(all_course_list, columns=columns)
df.to_csv("../../data/all_course.csv",index=False)



















