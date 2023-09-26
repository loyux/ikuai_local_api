import argparse
from ikuai_api.ikuai import Router


def cli(Router):
  parser = argparse.ArgumentParser(description='Process')

  parser.add_argument('-u',
                      '--username',
                        action='store_true',
                        default="xx",
                        help='路由器用户名')

  parser.add_argument('-p',
                      '--password',
                        action='store_true',
                        default="xx",
                        help='路由器登录密码')
  parser.add_argument('-P',
                      '--port',
                        action='store_true',
                        default=80,
                        help='路由器端口')
  parser.add_argument('-i',
                      '--ip',
                        action='store_true',
                        default="192.168.100.1",
                        help='路由器ip')

  args = parser.parse_args()

  route = Router(
      username=args.username, password=args.password, ip="192.168.100.1", port=80
  )

  route.get_cpu_info()
      
