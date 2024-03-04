import requests
import pandas as pd
from lxml import etree
import re
def get_headers(referer = None):
    """
    请求标头获取方法,返回k-v请求头
    @return: 字典，定制请求头header
    """
    headers = {}
    if referer is None:
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
            'cookie': 'EDUWEBDEVICE=6a0468f2094d4d66a96ac6326b1b9265; __yadk_uid=QPZLvPE09C5gW89IEWubY2zbYVXxfmuJ; WM_NI=xGSEJA0sfuIPIAcokUv%2BcYMd%2BQU0wUvxDMS6aDeueHnm4g7jHkUfVrb%2B3%2BTHw8Ymr063ieB3uU6TR3Cf8jr8U%2F7OgRN4O9NLwO9Ip2ZtZoQNbGWqgcHryVNzRSWcrCwxVjU%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeb6ed3aaf99ac9ad03391e78fb6c84b969e8facc840edab87a3c44f82b18cb3b52af0fea7c3b92abc999da6c94bf4adaa96cc5c8b9fad90ea5fb6f5adbad070e98f9bd1f65fb6a88caed23ea39cab96e844aeb3fc88b6628cb59b87d57aa2f5fdccd744b5e8978ef13cf6eda786c139b78bfab5d13981baf88bf13497f1f9b0e65a8eec81dacd48b591f7aaf33a9aac9690d446a2999992e6698caeb7b7cd72928d9984f149b5a89a8bd837e2a3; WM_TID=0vAboZxeEplEBUAREQaRsq7YVBUQ4SR%2F; NTESSTUDYSI=970502919303499c805cb0a6ba7bfcf1; utm="eyJjIjoiIiwiY3QiOiIiLCJpIjoiIiwibSI6IiIsInMiOiIiLCJ0IjoiIn0=|aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8="; Hm_lvt_77dc9a9d49448cf5e629e5bebaa5500b=1709296325,1709308941,1709348609; hb_MA-A976-948FFA05E931_source=github.com; NTES_YD_SESS=NJiPzSePd0TLV64JvLG4blfptYTOYKcOPAliYmHZY.DR0UVp0AITEqAQIIoeJbak4LKUFLd5B3lksxqd156Skjtu3OpEHIXBc0PrGzYP_3q43wkvW6FIwhc7917BMkYhvcRNN2HHBdZIqNiXAk6MFjjm9it_Agid2tpf0a_YABXad4fZ0ov0tpAsZqJSNFkwwqwXZ_kbSn2DMK.f1vcnBVByQskATfa_3f3FeHdJ_gsaF; NTES_YD_PASSPORT=cZJGtoP1HUWSaVKA11X6yAU32CEWlUL__xQH4EW_kTpQiAPuiaN2.Ha_NN6QjrYqhMXAdMSlKnpmUve9FTD5E00Nzlhyvc8UZsRaz.Kf4ZxpBuIGCEUaEw4KSwr4lbz8Xs1Hj3NnxMf3OugcyfpoIt3vs6LGN4sIFwz6hET3IFnLW4PKHz7vO.ZrWxXxI._2gLOE9fyMgD0OxZf21xOvCdeUv; STUDY_INFO="yd.d3727ed73b5c4150a@163.com|8|1548173032|1709350367622"; STUDY_SESS="RESYKVAkRXC2PMw9CtJDsdfWWpuh6uwj/F9iy9X3qXyB8QPSN6ZgDM1q4weCXm4eu9568KeT+z3lauRHqueL4XOov+nbeqMgk04Jja0AnxvS3ZvHxQtrYLdfKzJCgvO80nYCz/OrV9spGLL4glImKb2ak95MiBX8CR+tI/05UkQLhur2Nm2wEb9HcEikV+3FTI8+lZKyHhiycNQo+g+/oA=="; STUDY_PERSIST="ZNqFoOhuderKoMOW8a+62hgAs/EsOL8Ms2Q8H48ezDih/KkM4KmoT9OUiKgjiztkeWQHgOPcuBlTCLCNBhGLDbTgwozD80oJqbUF+PtMQcsO5KHt0DuQO7oz9/jsjkBVe8x8jtdP3Ow/nb7sG+yioDKNjIZSbg3olGJVg1sbmixRpN7pqCa/JZG9o/9xgfHJp37ZikDwAjmvlD6NcingLH51rzeuEe4qzdXBjg0eDJ7ZgpjCC7Iso4RP9U87vJE8LtaQzUT1ovP2MqtW5+L3Hw+PvH8+tZRDonbf7gEH7JU="; NETEASE_WDA_UID=1548173032#|#1678003498985; MOOC_PRIVACY_INFO_APPROVED=true; Hm_lpvt_77dc9a9d49448cf5e629e5bebaa5500b=1709350408'

        }
    else:
        headers = {
            'origin': 'https://www.icourse163.org',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
            'cookie':'EDUWEBDEVICE=027f379a49ef4388abe404d5fd4e477a; __yadk_uid=kxhdZKnO3Uo1zt5c0hxWy71nTyxFdfNi; WM_TID=%2F73o0LgVEDVABBBUQEPQ8r5KE7yUZu5v; NTESSTUDYSI=658b7b32976b43ba8e3e4f0ea563aaf2; Hm_lvt_77dc9a9d49448cf5e629e5bebaa5500b=1709180881,1709298680,1709356532,1709436947; hb_MA-A976-948FFA05E931_source=www.icourse163.org; WM_NI=F7TS%2FRoDLby%2BL%2FuSPyNuS%2FE4BZICg%2BlpnUAAFw%2FAZewzFR0cUZM%2FEHQA0RlIKPaaQRu5UyBynwb4UnZkbIwPZ07kFwtGg4rX%2BsSlilgLUFl5LOqFwYugfq5QaD5gnkCZUEI%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eed0bb4789ee0083b872abb08aa2c55a879b9f86c87e928f83d3fc42f59ffc93aa2af0fea7c3b92a86e99cb4ae5aad9c8483fc2190f1bbb4d3738eab9dd0c840828687a4e621b0b0a2b6c44b86a9e1a2d96fb5a68ab3b369978683d0c844939f00b3ef438990af82d45ab7eb9b9ac173aea9aed5d8669ab5aeaaf65c9af0f98cc57db899a9d5f154e9ad9d8dec68a5949ba7ef3f9091bfa7f653b7b9aa92b85ba39cfb88ed6181869ba6cc37e2a3; Hm_lpvt_77dc9a9d49448cf5e629e5bebaa5500b=1709452431',
            'referer': f'{referer}',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8'

        }
    return headers

def get_comment_headers(referer):
    headers ={
        'origin': 'https://www.icourse163.org',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'cookie': 'EDUWEBDEVICE=027f379a49ef4388abe404d5fd4e477a; __yadk_uid=kxhdZKnO3Uo1zt5c0hxWy71nTyxFdfNi; WM_TID=%2F73o0LgVEDVABBBUQEPQ8r5KE7yUZu5v; NTESSTUDYSI=fcb924b33b7342548d079a5b312ddb29; utm="eyJjIjoiIiwiY3QiOiIiLCJpIjoiIiwibSI6IiIsInMiOiIiLCJ0IjoiIn0=|aHR0cHM6Ly9jbi5iaW5nLmNvbS8="; hb_MA-A976-948FFA05E931_source=cn.bing.com; Hm_lvt_77dc9a9d49448cf5e629e5bebaa5500b=1709298680,1709356532,1709436947,1709520899; WM_NI=8STc0aXP84rrJS5cnmxLf84NzNP0XHDN5f6aNPrLywvP3tJutgQAK2Pb4h7oLiRlH6WvswObzrW7xJDFfiLUyj0cKh6%2Fxr902W%2B8M5Q2cvoNaOBmaVKJvjUPlHGPhDKRQnU%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eed6f573a192a3d6ec54b5ef8fb6c44a938a8bb0d83d978be5acc462a2ace1a3c12af0fea7c3b92afc8d9c84b36b9c90f8d5f17a8a8dfb84ed67bc94aad9b746ba92a0d1db448892fb87b56b8e90beadfc7db690fd95c97fb8b99fa2ca3a94befc89b66590b79e8dcb3e95aabd98ce6abaae99d8fb42889aaa8acf5fbbb60084ca64f6f1b893bc3cf289e5d9d03f93eead97ee46a3918e8ee45e8996ba8bd85cb09889b1eb50898e9f8fd837e2a3; Hm_lpvt_77dc9a9d49448cf5e629e5bebaa5500b=1709521081',
        'referer': 'https://www.icourse163.org/course/PKU-1470430188',
        'content-type': 'application/x-www-form-urlencoded'
    }
    return headers

def get_response(url,headers,data=None):
    """
    响应获取方法
    @param url: 目标url
    @param headers: 对应的请求头
    @param data: post请求data部分，非必须
    @return: 返回响应信息
    """
    if data is None:
        response = requests.get(url=url,headers=headers)
    else:
        response = requests.post(url=url, headers=headers,data=data)
    return response

def get_sort_name(school_list_cn,part_url_en,school_name):
    for i in range(len(school_list_cn)):
        if school_name == school_list_cn[i]:
            return part_url_en[i].split("/university/")[1]
    return None

def get_school_id():
    df = pd.read_csv('../../data/all_school.csv')   #路径由调用位置决定
    school_id = df['school_id'].tolist()
    return school_id

def get_post_data(schoolId,page):
    data = {
        'schoolId': f'{schoolId}',
        'p': f'{page}',
        'psize': '20',
        'courseStatus': '30',
        'type': '1'
    }
    return data

def get_comment_post_data(courseId,page):
    data = {
        'courseId': f"{courseId}",
        'pageIndex': f"{page}",
        'pageSize': '20',
        'orderBy': '3'
    }
    return data


def get_channel_post_data(channelId,page):
    data = {"mocCourseQueryVo": {"categoryId": -1, "categoryChannelId": channelId, "orderBy": 0, "stats": 30, "pageIndex": page,
                       "pageSize": 20}}
    return data
def course_json_to_list(json_data,all_list):
    courses = json_data['result']['list']
    for course in courses:
        # 课程id,课程名，学校名，学校简称，开始时间，教师id，教师姓名
        tmp = [course["id"], course["name"], course["schoolName"], course['schoolId'], course["teacherName"],
               course["teacherId"], course["enrollCount"], course["startTime"], course["endTime"], False]
        all_list.append(tmp)


def external_course_json_to_list(json_data,all_list):
    courses = json_data['result']['list']['mocCourseKyCardBulkPurchaseVo']
    # 编号（主键）、课程名称、教师名称、课程原价、课程售价、课程销售数、是否删除
    for course in courses:
        tmp = [course["courseId"], course["courseName"], course["teacherName"], course["originalPrice"], course["price"], course["enrollNum"],False]
        all_list.append(tmp)

def comment_json_to_list(json_data,course_id,all_list):
    comments = json_data['result']['list']
    for comment in comments:
        # 评论id，评论者id，评论课程id，评论者昵称，评论内容，用户评分，点赞数
        tmp = [comment["id"], comment["commentorId"], course_id, comment['userNickName'],comment['content'], comment["mark"],comment["agreeCount"]]
        all_list.append(tmp)


def get_course_id():
    df = pd.read_csv("../../data/all_course.csv")   #路径由调用位置决定
    course_id = df['id'].tolist()
    return course_id