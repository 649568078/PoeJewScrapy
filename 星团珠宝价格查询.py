import requests
import re
import time
import itertools
import json
import demjson
import os
import random
import sys

def get_item_info(payloadData, i, combinations):
    # POE根链接
    base_url = 'https://www.pathofexile.com/api/trade/search/Expedition'
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


def get_users_info(Result, Id, Total):
    # POE根链接
    base_url = "https://www.pathofexile.com/api/trade/fetch/"
    # 请求头设置
    payloadHeader = {'accept': '*/*',
                     'accept-encoding': 'gzip, deflate, br',
                     'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
                     #'referer': 'https://www.pathofexile.com/trade/search/Ritual/v5RgLUE',
                     'sec-fetch-dest': 'empty',
                     'sec-fetch-mode': 'cors',
                     'sec-fetch-site': 'same-origin',
                     'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
                     'x-requested-with': 'XMLHttpRequest'}
    # 调用get_items_info()的返回值Result和Id
    # 把之前res里的列表连接用逗号拼起来,并以十个为一组输出成真正的URL
    step = 10
    b = [Result[i:i + step] for i in range(0, len(Result), step)]
    print('b' + str(b))
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
        res = requests.post(real_url_list[0], headers=payloadHeader, timeout=10).text
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
        dic = {}
        # 获取价格表格

        currency = str(dic_List_format_i['listing']['price']['amount']) + str(
            dic_List_format_i['listing']['price']['currency'])

        dic['currency'] = currency
        currency_list.append(currency)

    return currency_list

# 物理持续对应表
test = [['Wound Aggravation', 'explicit.stat_69078820', 'pre'], ['Vivid Hues', 'explicit.stat_3957006524', 'pre'],
        ['Rend', 'explicit.stat_4263287206', 'pre'], ['Disorienting Wounds', 'explicit.stat_3351136461', 'pre'],
        ['Compound Injury', 'explicit.stat_4018305528', 'pre'],
        ['Blood Artist', 'explicit.stat_2284771334', 'pre'], ['Phlebotomist', 'explicit.stat_3057154383', 'pre'],
        ['Steady Torment', 'explicit.stat_3500334379', 'pre'],
        ['Wasting Affliction', 'explicit.stat_2066820199', 'pre'], ['Haemorrhage', 'explicit.stat_72129119', 'pre'],
        ['Flow of Life', 'explicit.stat_2350430215', 'pre'], ['Exposure Therapy', 'explicit.stat_131358113', 'pre'],
        ['Brush with Death', 'explicit.stat_2900833792', 'pre'],
        ['Vile Reinvigoration', 'explicit.stat_647201233', 'pre'],
        ['Circling Oblivion', 'explicit.stat_2129392647', 'pre'],
        ['Brewed for Potency', 'explicit.stat_3250272113', 'pre'],
        ['Student of Decay', 'explicit.stat_3202667190', 'pre'], ]

# 定义count_times
count_times = 2
# 定义珠宝空数量
jew_min_num = 5
jew_max_num = 6

# 定义文件名
file_name = '物理持续中型' + '.txt'

if not os.path.exists('combinations.txt'):
    # 遵循两前缀两后缀原则
    if count_times <= 2:
        combinations = list(itertools.combinations(test, count_times))
        print(combinations)
        c = 0
        for i in combinations:
            combinations[c] = list(i)
            c += 1
        combinations.reverse()
        with open('combinations.txt', 'w', encoding='utf-8-sig') as cb:
            cb.write(str(combinations))
        combinations = eval(open('combinations.txt', 'r', encoding='utf-8-sig').read())
    # 去除三缀一样的，不能出现三前缀或者三后缀
    else:
        combinations = list(itertools.combinations(test, count_times))
        c = 0
        for i in combinations:
            combinations[c] = list(i)
            c += 1
        combinations.reverse()
        for each_group in combinations[::-1]:
            fix_judge = []
            for each in each_group:
                fix_judge.append(each[2])
            if len(set(fix_judge)) == 1:
                # print(each_group)
                combinations.remove(each_group)
        with open('combinations.txt', 'w', encoding='utf-8-sig') as cb:
            cb.write(str(combinations))
        combinations = eval(open('combinations.txt', 'r', encoding='utf-8-sig').read())
else:
    combinations = eval(open('combinations.txt', 'r', encoding='utf-8-sig').read())

for i in combinations[::-1]:
    # (['Widespread Destruction', 'explicit.stat_1678643716', 'suf'],['Burning Bright', 'explicit.stat_4199056048', 'pre'], ['Lord of Drought', 'explicit.stat_2055715585', 'pre'])
    while True:
        print(len(combinations))
        print(i)
        print(str(i[0][1]))
        print(str(i[1][1]))
        if count_times == 2:
            payloadData = '{"query":{"status":{"option":"online"},"stats":[{"type":"and","filters":[{"id":"enchant.stat_3086156145","value":{"min":%s,"max":%s},"disabled":false},{"id":"%s"},{"id":"%s"}],"disabled":false}]},"sort":{"price":"asc"}}' % (jew_min_num,jew_max_num,str(i[0][1]),str(i[1][1]))
            print(payloadData)
        elif count_times == 3:
            payloadData = '{"query":{"status":{"option":"online"},"stats":[{"type":"and","filters":[{"id":"enchant.stat_3086156145","value":{"min":%s,"max":%s},"disabled":false},{"id":"%s"},{"id":"%s"},{"id":"%s"}],"disabled":false}]},"sort":{"price":"asc"}}' % (jew_min_num,jew_max_num,str(i[0][1]),str(i[1][1]),str(i[2][1]))
            print(payloadData)
        else:
            print('未知count_time')
            sys.exit()
        # 查询总览信息
        try:
            time.sleep(random.uniform(10, 12))
            items_info = get_item_info(payloadData, i, combinations)
            print()
            Result = items_info[0]
            Id = items_info[1]
            Total = items_info[2]
            # 先判断Result是否为空
            if Result == []:
                for a in i:
                    a.remove(a[1])
                print(i)
                print('[]')
                with open('价格表' + '\\' + file_name, 'a+', encoding='utf-8-sig') as file:
                    file.write(str(i) + '\n')
                    file.write('市场数量：' + str(Total) + '\n')
                    file.write(str('[]') + '\n')
                    file.write(str('-' * 50) + '\n')
                with open('分析表' + '\\' + file_name, 'a+', encoding='utf-8-sig') as file:
                    list_info = [str(i), '市场数量：' + str(Total), str('[]')]
                    file.write(str(list_info) + '\n')
                combinations.remove(i)

                with open('combinations.txt', 'w') as cb:
                    cb.write(str(combinations))
                break
            # 查询具体信息
            time.sleep(random.uniform(10, 12))
            users_info = get_users_info(Result, Id, Total)
            print(users_info)
            time.sleep(random.uniform(10, 12))
            currency_list = data_analysis_second(users_info)

            # 打印并写入
            for a in i:
                a.remove(a[1])

            print(i)
            print(currency_list)
            with open('价格表' + '\\' + file_name, 'a+', encoding='utf-8-sig') as file:
                file.write(str(i) + '\n')
                file.write('市场数量：' + str(Total) + '\n')
                file.write(str(currency_list) + '\n')
                file.write(str('-' * 50) + '\n')
            with open('分析表' + '\\' + file_name, 'a+', encoding='utf-8-sig') as file:
                list_info = [str(i), "市场数量：" + str(Total), str(currency_list)]
                file.write(str(list_info) + '\n')

            combinations.remove(i)
            with open('combinations.txt', 'w', encoding='utf-8-sig') as cb:
                cb.write(str(combinations))

        except Exception as e:
            print(e)
            continue

        break
