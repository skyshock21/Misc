#!/usr/bin/python3
#
# rand_ip.py
# A script to output random IP addresses

import random, struct, socket, argparse, sys
from random import getrandbits

# Function Defs
def rand_v4():
    return socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))

def rand_v6():
    return socket.inet_ntop(socket.AF_INET6, struct.pack('>QQ', getrandbits(64), getrandbits(64)))

# CLI arguments
ex = '''example:

python rand_ip.py
python rand_ip.py -v6 -n 10'''
parser = argparse.ArgumentParser(prog='rand_ip',
                                description='Returns a random IP address.',
                                epilog=ex,
                                formatter_class=argparse.RawDescriptionHelpFormatter,
                                )
group = parser.add_mutually_exclusive_group()
group.add_argument("-v4", "--ipv4", dest='func', action="store_const", const=rand_v4)
group.add_argument("-v6", "--ipv6", dest='func', action="store_const", const=rand_v6)
parser.add_argument("-n", 
                    "--number", 
                    type=int, 
                    help="Number of IPs to output",
                    default=1,
                   )
parser.set_defaults(func=rand_v4)
args = parser.parse_args()

def main():
    for i in range(args.number):
        print(args.func())

if __name__ == "__main__":
    sys.exit( main() )
