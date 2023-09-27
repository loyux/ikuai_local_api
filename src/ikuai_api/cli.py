import argparse
from ikuai_api.ikuai import Router
from rich.console import Console
import base64
import json
def cli():
    console = Console()
    parser = argparse.ArgumentParser(description="Process")

    subparser = parser.add_subparsers(help="子命令")
    parser_a = subparser.add_parser("login", help="login ikuai route")
    parser_a.add_argument(
        "-u", "--username", help="路由器用户名"
    )
    parser_a.add_argument(
        "-p", "--password", help="路由器登录密码"
    )
    parser_a.add_argument("-P", "--port", default=80, help="路由器端口")
    parser_a.add_argument(
        "-i", "--ip",  default="192.168.100.1", help="路由器ip"
    )    
    args = parser.parse_args()
    if args.username is None:
        console.print("""
usage: ikuai_cli [-h] [-u USERNAME] [-p PASSWORD] [-P PORT] [-i IP]

Process

options:
  -h, --help            show this help message and exit
  -u USERNAME, --username USERNAME
                        路由器用户名
  -p PASSWORD, --password PASSWORD
                        路由器登录密码
  -P PORT, --port PORT  路由器端口
  -i IP, --ip IP        路由器ip
""")
    else:
        route = Router()
        route.insert_route_info(username=str(args.username), password=str(args.password), ip="192.168.100.1", port=80)
        resp = route.get_cpu_info()
        print(resp.text)

cli()