import requests
import re
import time
import itertools
import json
import demjson
import os
import random
import sys
import threading
from concurrent.futures import ThreadPoolExecutor
import pickle
import traceback
import ndjson
import pymysql
from JewList import Jewlist
import datetime

# 全局变量
conn = pymysql.connect(host='10.33.12.96', user='root', password='xx19941130', database='poe')
if conn:
    print('正常连接')
cursor = conn.cursor()
lock = threading.Lock()
lock2 = threading.Lock()

dummy_event = threading.Event()


def write_to_database(sql):
    lock.acquire()  # 锁
    try:
        with conn.cursor() as cursor:
            # 在这里执行写入数据库的操作
            cursor.execute(sql)
        conn.commit()
    except pymysql.Error as e:
        print(f"Error: {e}")
    finally:
        lock.release()
    return


def insert_sql(conn, cursor, tablename, toinserts_values):
    keys = ", ".join(toinserts_values.keys())
    qmark = ", ".join(["%s"] * len(toinserts_values))
    sql_insert = "insert into %s (%s) values (%s)" % (tablename, keys, qmark)
    try:
        cursor.execute(sql_insert, list(toinserts_values.values()))
        conn.commit()
    except Exception as e:
        print(e)
        print(sql_insert)
        conn.rollback()
        print("插入失败")


def get_item_info_threading(payloadData, t_sequence):
    proxies_copy = proxies.copy()
    Result, Id, Total = "", "", ""
    proxie = proxies_copy[int(t_sequence)]
    print(str(proxie))
    # POE根链接
    base_url = 'https://www.pathofexile.com/api/trade/search/Ancestor'
    # 请求头设置
    payloadHeader = {'accept': '*/*',
                     'accept-encoding': 'gzip, deflate, br',
                     'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
                     'content-length': '282',
                     'content-type': 'application/json',
                     'origin': 'https://www.pathofexile.com',
                     'sec-fetch-dest': 'empty',
                     'sec-fetch-mode': 'cors',
                     'sec-fetch-site': 'same-origin',
                     'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
                     'x-requested-with': 'XMLHttpRequest'}
    # 设置重连次数
    requests.adapters.DEFAULT_RETRIES = 3
    # 设置连接活跃状态为False
    s = requests.session()
    s.keep_alive = False
    # 使用requests库发送请求post
    try:
        res = requests.post(base_url, data=payloadData, headers=payloadHeader, timeout=10, proxies=proxie)
        res_text = res.text
    except Exception:
        print("错误" + str(traceback.format_exc()))
        get_one_proxies(t_sequence)
        res = "None"
        res_text = "None"
    print('第一步res' + res_text)
    Result = res.json()["result"]
    Id = res.json()["id"]
    Total = res.json()["total"]
    return Result, Id, Total


def get_users_info_threading(Result, Id, Total, t_sequence):
    proxies_copy = proxies.copy()
    res = ""
    proxie = proxies_copy[int(t_sequence)]
    print(str(proxie))
    # POE根链接
    base_url = "https://www.pathofexile.com/api/trade/fetch/"
    # 请求头设置
    payloadHeader = {'accept': '*/*',
                     'accept-encoding': 'gzip, deflate, br',
                     'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
                     'sec-fetch-dest': 'empty',
                     'sec-fetch-mode': 'cors',
                     'sec-fetch-site': 'same-origin',
                     'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
                     'x-requested-with': 'XMLHttpRequest'}
    # 调用get_items_info()的返回值Result和Id
    # 把之前res里的列表连接用逗号拼起来,并以十个为一组输出成真正的URL
    step = 10
    b = [Result[i:i + step] for i in range(0, len(Result), step)]
    # print('b' + str(b))
    real_url_list = []
    for i in b:
        Result_for = ','.join(i)
        real_url = base_url + Result_for + "?query=" + str(Id)
        real_url_list.append(real_url)
    # 使用requests库发送请求post
    # 设置重连次数
    requests.adapters.DEFAULT_RETRIES = 3
    # 设置连接活跃状态为False
    s = requests.session()
    s.keep_alive = False
    # print(real_url_list)
    if real_url_list != []:
        try:
            res = requests.post(real_url_list[0], headers=payloadHeader, timeout=10, proxies=proxie).text
            # print(res)
        except Exception:
            print("错误" + str(traceback.format_exc()))
            get_one_proxies(t_sequence)
    else:
        res = '人员信息拼串出错，可能为空'
    return res


def get_item_info(payloadData, t_sequence):
    res, Result, Id, Total = "", "", "", ""
    # POE根链接
    base_url = 'https://www.pathofexile.com/api/trade/search/Ancestor'
    # 请求头设置
    payloadHeader = {'accept': '*/*',
                     'accept-encoding': 'gzip, deflate, br',
                     'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
                     'content-length': '282',
                     'content-type': 'application/json',
                     'origin': 'https://www.pathofexile.com',
                     'sec-fetch-dest': 'empty',
                     'sec-fetch-mode': 'cors',
                     'sec-fetch-site': 'same-origin',
                     'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
                     'x-requested-with': 'XMLHttpRequest'}
    # 设置重连次数
    requests.adapters.DEFAULT_RETRIES = 3
    # 设置连接活跃状态为False
    s = requests.session()
    s.keep_alive = False
    # 使用requests库发送请求post
    res = requests.post(base_url, data=payloadData, headers=payloadHeader, timeout=10)
    res_text = res.text
    print('第一步res' + res_text)
    Result = res.json()["result"]
    Id = res.json()["id"]
    Total = res.json()["total"]
    return Result, Id, Total


def get_users_info(Result, Id, Total, t_sequence):
    proxies_copy = proxies.copy()
    res = ""
    # POE根链接
    base_url = "https://www.pathofexile.com/api/trade/fetch/"
    # 请求头设置
    payloadHeader = {'accept': '*/*',
                     'accept-encoding': 'gzip, deflate, br',
                     'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
                     'sec-fetch-dest': 'empty',
                     'sec-fetch-mode': 'cors',
                     'sec-fetch-site': 'same-origin',
                     'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
                     'x-requested-with': 'XMLHttpRequest'}
    # 调用get_items_info()的返回值Result和Id
    # 把之前res里的列表连接用逗号拼起来,并以十个为一组输出成真正的URL
    step = 10
    b = [Result[i:i + step] for i in range(0, len(Result), step)]
    # print('b' + str(b))
    real_url_list = []
    for i in b:
        Result_for = ','.join(i)
        real_url = base_url + Result_for + "?query=" + str(Id)
        real_url_list.append(real_url)
    # 使用requests库发送请求post
    # 设置重连次数
    requests.adapters.DEFAULT_RETRIES = 3
    # 设置连接活跃状态为False
    s = requests.session()
    s.keep_alive = False
    # print(real_url_list)
    if real_url_list != []:
        try:
            res = requests.post(real_url_list[0], headers=payloadHeader, timeout=10).text
            print(res)
        except Exception as e:
            print("错误" + str(e))
    else:
        res = '人员信息拼串出错，可能为空'
    return res


def data_analysis_second(users_info):
    currency_list = []
    item_info_list = []

    # 取得之前提取的JS信息
    i = users_info
    format_i = demjson.decode(i)  # str({[]})→{[]}

    # 通过对字典的取键，得到一个列表值
    List_formated_i = format_i['result']  # {[{},{},{}]}→[{},{},{}]
    # 列表里面是一个个的玩家信息字典，通过循环依次去到
    count = 0
    for dic_List_format_i in List_formated_i:
        # print("dic_List_format_i",dic_List_format_i)
        dic = {}
        # 获取价格表格

        currency = str(dic_List_format_i['listing']['price']['amount']) + str(
            dic_List_format_i['listing']['price']['currency'])

        dic['currency'] = currency
        currency_list.append(currency)

    return currency_list


def get_proxies():
    # 提取代理API接口，获取代理IP
    api_url = "http://webapi.http.zhimacangku.com/getip?num=10&type=2&pro=&city=0&yys=0&port=11&pack=231713&ts=0&ys=0&cs=0&lb=1&sb=0&pb=5&mr=1&regions="
    proxy_ips = requests.get(api_url).text.replace('false', 'False').replace('true', 'True').replace('null', '""')
    print(proxy_ips)
    proxy_ips = eval(proxy_ips)['data']
    proxies_list = []
    for proxy_ip in proxy_ips:
        ip = proxy_ip["ip"]
        port = proxy_ip["port"]
        proxyMeta = "http://%(host)s:%(port)s" % {
            "host": ip,
            "port": port,
        }
        pro = {'http': proxyMeta, 'https': proxyMeta}
        proxies_list.append(pro)
    f = open("proxies.pkl", 'wb')
    pickle.dump(proxies_list, f)
    return


def get_one_proxies(t_sequence):
    # 提取代理API接口，
    with lock2:
        api_url = "http://webapi.http.zhimacangku.com/getip?num=1&type=2&pro=&city=0&yys=0&port=11&pack=231713&ts=0&ys=0&cs=0&lb=1&sb=0&pb=5&mr=2&regions="
        proxy_ips = requests.get(api_url).text.replace('false', 'False').replace('true', 'True').replace('null', '""')
        print(proxy_ips)
        proxy_ips = eval(proxy_ips)['data']
        for proxy_ip in proxy_ips:
            ip = proxy_ip["ip"]
            port = proxy_ip["port"]
            proxyMeta = "http://%(host)s:%(port)s" % {
                "host": ip,
                "port": port,
            }
            pro = {'http': proxyMeta, 'https': proxyMeta}
            proxies[int(t_sequence)] = pro
        print("线程{}替换IP代理".format(int(t_sequence)))
        f = open("proxies.pkl", 'wb')
        pickle.dump(proxies, f)
    # 线程等待
    dummy_event.wait(timeout=10)
    return


def proxies_test(proxies_list):
    # 要访问的目标网页
    target_url = "https://dev.kdlapi.com/testproxy"
    for each in proxies_list:
        # 使用代理IP发送请求
        try:
            print('try' + str(each))
            response = requests.get(target_url, proxies=each, timeout=5)
            # 获取页面内容
            if response.status_code == 200:
                print(response.text)
            else:
                print(response.status_code)
        except:
            proxies_list.remove(each)

    return proxies_list


def add_explicit(ref):
    # 读取ndjson
    anno_data = ndjson.load(open('./stats.ndjson'))
    count = 0
    explicit = ''
    ref = "Added Passive Skill is {}".format(ref)
    for anno in anno_data:
        if ref in anno['ref']:
            try:
                explicit = anno['trade']['ids']['explicit']
            except:
                print(ref)
                print(anno['ref'])
                sys.exit()
            if len(explicit) == 1:
                explicit = explicit[0]
            else:
                print('{}的explicit大于1'.format(anno['ref']))
            count += 1
    if count != 1:
        print('{}count有问题,数值是{}'.format(ref, count))
        sys.exit()
    else:
        return explicit


def make_combination_sql():
    # 创建星团价格统计表
    creat_table_sql = """
                         CREATE TABLE IF NOT EXISTS {} (
                             ID TEXT,
                             词缀一 TEXT,
                             词缀二 TEXT,
                             词缀三 TEXT,
                             payload TEXT,
                             url TEXT,
                             所属星团 TEXT,
                             市场数量 TEXT,
                             价格区间 TEXT,
                             平均价格 TEXT,
                             处理日期 TEXT);""".format(file_name)
    cursor.execute(creat_table_sql)
    # 创建对应关系
    together_list = Jewlist().together_mid()  # 选择星团
    for Jew, Jew_name in together_list:
        count_times = 2  # 定义count_times
        jew_min_num = 4  # 定义珠宝空数量
        jew_max_num = 5

        # 星团explicit化
        for each in Jew:
            each_ref = each[0]
            explicit = add_explicit(each_ref)
            each.insert(1, explicit)  # 在元素1的位置插入explicit，不改变原来的结构
        print("词条add_explicit化后形态为{}".format(Jew))

        # 写入数据库
        # 遵循两前缀两后缀原则
        if count_times <= 2:
            combinations = list(itertools.combinations(Jew, count_times))
            c = 0
            for i in combinations:
                combinations[c] = list(i)
                c += 1
            combinations.reverse()
        # 关于三词缀的属性
        else:
            combinations = list(itertools.combinations(Jew, count_times))
            c = 0
            for i in combinations:
                combinations[c] = list(i)
                c += 1
            combinations.reverse()
            # 移除三缀一样的词条
            for each_group in combinations[::-1]:
                fix_judge = []
                for each in each_group:
                    print("each{}".format(each[2]))
                    fix_judge.append(each[2])
                if len(set(fix_judge)) == 1:
                    # print(each_group)
                    combinations.remove(each_group)
            # 理论上没有两后缀一前缀这里做一个设置
            pass

        for i in combinations:
            insert_dict = {}
            # 写入payloadData
            if count_times == 2:
                explicit1 = str(i[0][1])
                explicit2 = str(i[1][1])
                insert_dict['词缀一'] = str(i[0][0])
                insert_dict['词缀二'] = str(i[1][0])
                payloadData = '{"query":{"status":{"option":"online"},"stats":[{"type":"and","filters":[{"id":"enchant.stat_3086156145","value":{"min":%s,"max":%s},"disabled":false},{"id":"%s"},{"id":"%s"}],"disabled":false}]},"sort":{"price":"asc"}}' % (
                    jew_min_num, jew_max_num, explicit1, explicit2)
            elif count_times == 3:
                explicit1 = str(i[0][1])
                explicit2 = str(i[1][1])
                explicit3 = str(i[2][1])
                insert_dict['词缀一'] = str(i[0][0])
                insert_dict['词缀二'] = str(i[1][0])
                insert_dict['词缀三'] = str(i[2][0])
                payloadData = '{"query":{"status":{"option":"online"},"stats":[{"type":"and","filters":[{"id":"enchant.stat_3086156145","value":{"min":%s,"max":%s},"disabled":false},{"id":"%s"},{"id":"%s"},{"id":"%s"}],"disabled":false}]},"sort":{"price":"asc"}}' % (
                    jew_min_num, jew_max_num, explicit1, explicit2, explicit3)
            else:
                print('未知count_time')
                sys.exit()
            insert_dict['payload'] = payloadData
            insert_dict['所属星团'] = Jew_name
            insert_sql(conn, cursor, file_name, insert_dict)
    return


def avg_currencycount(currency_list):
    # 开始循环
    currency_list = eval(currency_list)
    # 定义DIV比率
    chao_div = float(230)
    chao_ex = float(15)
    judge_list = []
    print(currency_list)
    for each in currency_list:
        if re.search('([\d|.]*)chaos', each):
            each = float(re.search('([\d|.]*)chaos', each).group(1))
            judge_list.append(each)
        elif re.search('([\d|.]*)divine', each):
            each = float(re.search('([\d|.]*)divine', each).group(1))
            # 定义货币统一标准
            each = each * chao_div
            judge_list.append(each)
        elif re.search('([\d|.]*)exalted', each):
            each = float(re.search('([\d|.]*)exalted', each).group(1))
            # 定义货币统一标准
            each = each * chao_ex
            judge_list.append(each)
        else:
            pass
    # 去掉第一个最低值，后三个值求平均数，如果去掉第一个值
    if len(judge_list) != 0:
        if len(judge_list) >= 4:
            judge_value = (judge_list[1] + judge_list[2] + judge_list[3]) / 3
        elif len(judge_list) == 1:
            judge_value = judge_list[0]
        else:  # 如果小于四，大于1，则计算普通平均值
            judge_value = 0
            for i in range(1, len(judge_list) + 1):
                judge_value += judge_list[i - 1]
            judge_value = judge_value / len(judge_list)
    else:
        judge_value = 0
    return round(judge_value, 2)  # 返回两位小数


def craw(payload):
    # 打印线程名字
    t = threading.currentThread()
    print(t.getName())
    print(payload)
    # 线程编号
    if max_workers == 1:
        t_sequence = 0
    else:
        t_sequence = re.search('ThreadPoolExecutor-0_(.)', t.getName()).group(1)
    id = payload[0]
    payloadData = payload[1]
    print(id)
    print(payloadData)
    # 查询物品信息
    if claw_type == 0:
        items_info = get_item_info_threading(payloadData, t_sequence)
    elif claw_type == 1:
        items_info = get_item_info(payloadData, t_sequence)
    else:
        print('检查claw_type')
        sys.exit()
    print('第二步items_info' + str(items_info))
    Result = items_info[0]
    Id = items_info[1]
    Total = items_info[2]
    url = 'https://www.pathofexile.com/trade/search/Ancestor/{}'.format(Id)
    try:
        # 查询具体信息
        # 进行Result判断
        # Result会有如下内容.[]服务器返回了没内容,''第一步请求没有正确请求到,["dsafsadf"]服务器正确返回了数据
        data = datetime.date.today()
        if Result != '' and Result != []:
            if claw_type == 0:
                users_info = get_users_info_threading(Result, Id, Total, t_sequence)
            elif claw_type == 1:
                users_info = get_users_info(Result, Id, Total, t_sequence)
            else:
                print('检查claw_type')
                sys.exit()
        elif Result == []:
            update_sql = f"""UPDATE {file_name} SET 市场数量 = '0', 价格区间 = '[]',  处理日期  = '{data}' WHERE id = {id};"""
            write_to_database(update_sql)
            return
        else:
            return  # 如果第一步没获取到，就直接return，下次执行的时候再爬
        # print('第三步users_info' + str(users_info))
        # users_info有三种状态，''，["内容"], "人员信息拼串出错，可能为空"
        if users_info == '' and Result != []:  # 第一步爬下来了，第二步没爬下来，可能是代理失效，略过等下次爬取
            return
        elif users_info == "人员信息拼串出错，可能为空":
            print('人员信息拼串出错，可能为空')
            sys.exit()
        else:
            # print(3)
            currency_list = data_analysis_second(users_info)
        # 打印并写入
        print(currency_list)
        update_sql = f"""UPDATE {file_name} SET 市场数量 = "{Total}", 价格区间 = "{currency_list}", 处理日期  = "{data}"  WHERE id = "{str(Id)}";"""
        print(update_sql)
        write_to_database(update_sql)
    except Exception:
        print("错误" + str(traceback.format_exc()))
    # 线程等待
    dummy_event.wait(timeout=20)


def main():
    # 获取代理
    get_proxies()
    global proxies
    proxies = pickle.load(open('proxies.pkl', 'rb'))
    print('获取到的IP数量:' + str(len(proxies)))
    print(proxies)

    global file_name
    file_name = '星团价格统计表20231214'

    # 检测代理IP可用性
    #proxies = proxies_test(proxies)

    # #根据词缀生成payload
    #make_combination_sql()

    # 查询还没搜索的星团
    sqlstr = f"""SELECT id,payload FROM {file_name} WHERE 价格区间 IS NULL;"""
    cursor.execute(sqlstr)
    result = cursor.fetchall()

    # payload_list读取
    payload_list = []
    for i in result:
        payload_list.append(i)

    # # #多线程处理组合,爬取+对combinations进行修改，max_workers和爬取代理IP数同步
    global max_workers
    global claw_type
    max_workers = 10
    claw_type = 1  # 选择爬取方式,0为每个线程一个IP，1为每个线程循环IP
    # 对claw_type的要求
    if claw_type == 1:
        max_workers = 1

    pool = ThreadPoolExecutor(max_workers=max_workers)
    pool.map(craw, payload_list)

    # craw(payload_list[0])

    # 计算平均价格
    sqlstr = f"""SELECT id,价格区间 FROM {file_name} WHERE 平均价格 IS NULL and 价格区间 IS NOT NULL;"""
    cursor.execute(sqlstr)
    result = cursor.fetchall()
    # 读取
    for i in result:
        avg_id = i[0]
        currency_list = i[1]
        avg_price = avg_currencycount(currency_list)
        update_sql = f"""UPDATE {file_name} SET 平均价格 = '{avg_price}' WHERE id = '{avg_id}';"""

        cursor.execute(update_sql)
    conn.commit()


if __name__ == '__main__':
    main()
