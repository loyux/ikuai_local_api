import ikuai
import argparse
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('username', type=str, help='an input variable')
    parser.add_argument('password', type=str, help='an input variable')
    args = parser.parse_args()
    route = ikuai.Router(
        username=args.username, password=args.password, ip="192.168.100.1", port=80
    )
    route.get_cpu_info()
    
