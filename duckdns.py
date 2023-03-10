import requests
def __bind_for_duckdns_core__(ip_to_domain:list[(str,str)], duckdns_token:str):
# """利用duckdns的服务，获取免费ddns的域名，将动态域名绑定"""
    for ip,domain in ip_to_domain:
        url = f"https://www.duckdns.org/update?domains={domain}&token={duckdns_token}&ip={ip}"
        resp = requests.get(url)
        print(resp.status_code,resp.text)