## Ikuai本地部分api

路由:爱快免费版3.6.13 x64 Build202301131532

功能
1. 获取路由lan/wan/cpu等信息
```python
route = ikuai.Router(
        username="xxx", password="xxx", ip="10.10.10.1", port=80
    )
    #获取wan的信息
    d = route.get_wan_info()
    for i in d:
        print(i.ip_addr)
    #获取lan的信息
    d = route.get_lan_info()
    for i in d:
        print(i.ip_addr)
```
2. 端口映射配置
```
resp = route.dport_add(lan_addr="192.168.100.100", lan_port="3389",wan_port="3389")
```
3. 配置l2tp等


4. 从pip安装使用
```
pip install 