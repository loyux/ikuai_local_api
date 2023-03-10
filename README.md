## Ikuai本地部分api

路由:爱快免费版3.6.13 x64 Build202301131532

### install && how to use

```bash
pip install git+https://github.com/loyurs/ikuai_local_api.git
```

1. 获取路由lan/wan/cpu等信息
```python
from ikuai_local_api import ikuai
router = ikuai.Router(ip="",port=80,username="xx",password="xx")
router.get_cpu_info()
lan = router.get_lan_info()
#多条lan线路
for i in lan:
    print(i.ip_addr)
    print(i.client_device)
```



2. 端口映射配置
```python
from ikuai_local_api import ikuai
router = ikuai.Router(ip="",port=80,username="xx",password="xx")
resp = route.dport_add(lan_addr="192.168.100.100", lan_port="3389",wan_port="3389")
```

3. 配置l2tp
etc..
