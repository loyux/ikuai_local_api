from ikuai_api.ikuai import Router
# from rich.console import Console
# console = Console()

router =Router()
r = router.insert_route_info("admin", "li19960124", "192.168.100.1")
print(r)
resp = router.__get_dport_show__()
print(resp.text)
