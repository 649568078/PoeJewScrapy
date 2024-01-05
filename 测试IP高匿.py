import requests
import time

def get_proxies():
    # 提取代理API接口，获取1个代理IP
    api_url = "http://webapi.http.zhimacangku.com/getip?num=5&type=2&pro=&city=0&yys=0&port=11&time=1&ts=0&ys=0&cs=0&lb=1&sb=0&pb=5&mr=1&regions="

    proxy_ips = requests.get(api_url).text.replace('false', 'False').replace('true', 'True').replace('null','""')
    print(proxy_ips)
    proxy_ips = eval(proxy_ips)['data']
    proxies_list = []
    for proxy_ip in proxy_ips:
        ip = proxy_ip["ip"]
        port = proxy_ip["port"]
        proxies = {}
        proxyMeta = "http://%(host)s:%(port)s" % {
            "host": ip,
            "port": port,
        }
        proxies['http'] = proxyMeta
        proxies_list.append(proxies)
    print(proxies_list)

    return proxies_list

def proxies_test(proxies_list):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"}
    # 要访问的目标网页
    target_url = "http://httpbin.org/get?show_env=1"
    for each in proxies_list:
        print(each)
        # 使用代理IP发送请求
        try:
            response = requests.get(target_url, proxies=each,headers=headers,timeout=5)
            # 获取页面内容
            if response.status_code == 200:
                print(response.text)
            else:
                print(response.text)
        except Exception as e:
            proxies_list.remove(each)
            print(e)
        time.sleep(1)
    return proxies_list

#proxies_list = get_proxies()
proxies_list = [{'http': 'http://117.69.30.190:9999'}]
proxies_test(proxies_list)

