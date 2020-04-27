import datetime
import time

def formatDate(obj, type):
    if isinstance(obj, datetime.datetime) and type=='Y-m-d H-M-S':
        return obj.strftime('%Y-%m-%d %H:%M:%S')

    elif isinstance(obj, datetime.date) and type=='Y-m-d':
        return obj.strftime("%Y-%m-%d")
    
    else :
        return ''

def formatDate2(obj, type):
    """
    时间戳转时间
    """
    time_local = time.localtime(obj)#格式化时间戳为本地时间
    # time_YmdHMS = time.strftime("%Y%m%d_%H%M%S",time_local)#自定义时间格式
    if type=='Y-m-d H-M-S':
        return time.strftime("%Y--%m--%d %H:%M:%S",time_local)

    elif type=='Y-m-d':
        return time.strftime("%Y-%m-%d",time_local)
    
    else :
        return ''

def formatDate3(obj):
    """
    时间转时间戳
    """
    return ''
    