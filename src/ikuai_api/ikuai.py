import requests
import json
import base64
import hashlib

"""
路由:爱快免费版3.6.13 x64 Build202301131532
功能
1. 获取路由lan/wan/cpu等信息
2. 端口映射配置
"""
from dataclasses import dataclass
import json


@dataclass
class AdslInfo:
    """wan Python object"""

    id: int
    interface: str
    parent_interface: str
    ip_addr: str
    gateway: str
    internet: str
    updatetime: str
    auto_switch: str
    result: str
    errmsg: str
    comment: str


from dataclasses import dataclass


@dataclass
class LanDeviceInfo:
    """LAN python Object"""

    apmac: str
    ssid: str
    id: int
    downrate: str
    webid: int
    uprate: str
    total_up: int
    total_down: int
    mac: str
    reject: int
    uptime: str
    hostname: str
    dtalk_name: str
    timestamp: int
    frequencies: str
    bssid: str
    signal: str
    ip_addr_int: int
    connect_num: int
    upload: int
    download: int
    auth_type: int
    client_type: str
    client_device: str
    ip_addr: str
    apname: str
    ac_gid: int
    comment: str
    username: str
    ppptype: str


LOGIN_IN = "/Action/login"
CALL_API = "/Action/call"


class Router:
    def __init__(
        self,
    ) -> None:
        """初始化登录认证"""
        self.password = None
        self.ip = None
        self.port = 80
        self.username = None
        
    def insert_route_info(self, username, password, ip, port=80):
        self.ip = ip
        self.port = port
        self.username = username
        self.password = password
        self.base_url = f"http://{self.ip}:{self.port}"
        self.__encode_password__()
        data = {
            "username": self.username,
            "passwd": self.md5_password,
            "pass": self.__encode_pass__(),
            "remember_password": "",
        }
        self.session = requests.Session()
        self.session.headers.update(
            {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
                "Accept": "application/json",
                "Content-type": "application/json;charset=utf-8",
                "Accept-Language": "zh-CN",
            }
        )
        self.call_url = self.base_url + CALL_API
        # data = {"username": username, "passwd": self.password}
        login_in_status = self.session.post(
            f"{self.base_url}{LOGIN_IN}", data=json.dumps(data)
        )
        return login_in_status.text




    def get_lan_info(self) -> list[LanDeviceInfo]:
        """获取lan的接入信息"""
        payload = {
            "func_name": "monitor_lanip",
            "action": "show",
            "param": {
                "TYPE": "data,total",
                "ORDER_BY": "ip_addr_int",
                "orderType": "IP",
                "limit": "0,20",
                "ORDER": "",
            },
        }
        url = self.base_url + CALL_API
        resp = self.session.post(url, data=json.dumps(payload))
        # 转换为字典
        dict_s = json.loads(resp.text)
        dict_dst = dict_s.get("Data").get("data")
        sum_list_obj = []
        for i in dict_dst:
            d = json.dumps(i)
            data = json.loads(d)
            single = LanDeviceInfo(**data)
            sum_list_obj.append(single)
        return sum_list_obj

    def get_wan_info(self) -> list[AdslInfo]:
        """获取wan口的接入信息"""
        payload = {
            "func_name": "monitor_iface",
            "action": "show",
            "param": {"TYPE": "iface_check,iface_stream,ether_info,snapshoot"},
        }
        resp = self.session.post(self.call_url, data=json.dumps(payload))
        # 将str转换为字典
        datas = json.loads(resp.text)
        # print(type(datas))
        # print(datas)
        # 从字典中获取需要的字段
        wan_info_list = datas.get("Data").get("iface_check")
        wan_info_python_obj_list = []
        for i in wan_info_list:
            # 将dict转换为str
            d = json.dumps(i)
            # 将str转换为json
            data = json.loads(d)
            # 将json转换为python object
            adsl_info = AdslInfo(**data)
            wan_info_python_obj_list.append(adsl_info)
        return wan_info_python_obj_list

    def get_cpu_info(self):
        payload = {
            "func_name": "sysstat",
            "action": "show",
            "param": {"TYPE": "verinfo,cpu,memory,stream,cputemp"},
        }
        url = self.base_url + CALL_API
        resp = self.session.post(url, data=json.dumps(payload))
        return resp

    def __more__():
        pass

    def get_l2tp_online_users(self):
        payload = {
            "func_name": "ppp_online",
            "action": "show",
            "param": {
                "TYPE": "data,total",
                "FINDS": "username,name,ip_addr,mac,phone,comment",
                "KEYWORDS": "",
                "limit": "0,20",
                "ORDER_BY": "",
                "ORDER": "",
            },
        }
        url = self.base_url + CALL_API
        resp = self.session.post(url, data=json.dumps(payload))
        return resp

    def __get_dport_show__(self):
        show_payload = {
            "func_name": "dnat",
            "action": "show",
            "param": {
                "TYPE": "total,data",
                "limit": "0,20",
                "ORDER_BY": "",
                "ORDER": "",
            },
        }
        resp = self.session.post(self.call_url, data=json.dumps(show_payload))
        return resp

    def dport_add(
        self,
        lan_addr,
        wan_port,
        lan_port,
        protocol="tcp+udp",
        interface="adsl1,adsl2.adsl3",
        enabled="yes",
        comment="www",
        src_addr="",
    ):
        """获取端口映射信息
        更改端口映射
        """
        payload_add = {
            "func_name": "dnat",
            "action": "add",
            "param": {
                "enabled": enabled,
                "comment": comment,
                "interface": interface,
                "lan_addr": lan_addr,
                "protocol": protocol,
                "wan_port": wan_port,
                "lan_port": lan_port,
                "src_addr": src_addr,
            },
        }
        resp = self.session.post(self.call_url, data=json.dumps(payload_add))
        return resp

    def dport_delete(self, dport_id: int):
        """根据ikuai 的端口映射删除ikuai的端口映射，根据id进行删除"""
        payload = {"func_name": "dnat", "action": "del", "param": {"id": dport_id}}
        resp = self.session.post(self.call_url, json.dumps(payload))
        return resp

    def __encode_password__(self):
        md5 = hashlib.md5()
        md5.update(self.password.encode())
        hash_value = md5.hexdigest()
        self.md5_password = hash_value

    def __encode_pass__(self) -> str:
        d = ("salt_11" + self.password).encode("ASCII")
        encode_pass = base64.b64encode(d).decode()
        return encode_pass

    def __create_l2tp__(self, ipsec_secret:str):
        """快速创建l2tp规则
            macos/ios可以使用自带vpn进行连接
        """
        payload = {
            "func_name": "l2tp_server",
            "action": "save",
            "param": {
                "dns1": "114.114.114.114",
                "dns2": "114.114.115.115",
                "mtu": 1400,
                "mru": 1400,
                "ipsec_secret": ipsec_secret,
                "id": 1,
                "enabled": "yes",
                "force_ipsec": 1,
                "server_ip": "10.1.0.1",
                "rightid": "",
                "server_port": 1701,
                "addr_pool": "10.1.0.2-10.1.0.254",
                "leftid": "",
            },
        }
        resp = self.session.post(self.call_url, data = json.dumps(payload))
        return resp