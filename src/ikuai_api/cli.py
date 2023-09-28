import argparse
from ikuai_api.ikuai import Router
from rich.console import Console
def cli():
    console = Console()
    parser = argparse.ArgumentParser(description="Process")
    subparser = parser.add_subparsers(help="sub command")
    parser_auth = subparser.add_parser("login", help="login ikuai route")
    parser_auth.add_argument(
        "-u", "--username", help="路由器用户名"
    )
    parser_auth.add_argument(
        "-p", "--password", help="路由器登录密码"
    )
    parser_auth.add_argument("-P", "--port", default=80, help="路由器端口")
    parser_auth.add_argument(
        "-i", "--ip",  default="192.168.100.1", help="路由器ip"
    )

    # show command
    parser_show = subparser.add_parser("show", help="show router info")
    parser_show.add_argument("-l", "--lan-info", help="show lan info")
    parser_show.add_argument("-d", "--port-forward", help="端口转发信息")
    args = parser.parse_args()._get_args()
    if len(args) == 0:
        console.print("""
usage: cli.py [-h] {login,show} ...

Process

positional arguments:
  {login,show}  sub command
    login       login ikuai route
    show        show router info

options:
  -h, --help    show this help message and exit
""")
        exit(0)


    print(args)
    route = Router()
    route.insert_route_info(username=str(args.username), password=str(args.password), ip="192.168.100.1", port=80)
    resp = route.get_cpu_info()
    if resp.status_code != 200:
        console.print("Please use -h")    
    else:
        print(resp.text)