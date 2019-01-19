#!/usr/bin/env python
#
# rand_ip.py
# A script to output random IP addresses

# TO-DO:
# create flag for generating multiple IPs (-n 10)
# add_argument('-n', '--number', action='store', dest='number', type=int, default=1, help='number of IPs')
# refactor first if check in main to check for null flags
# as if not len(sys.argv) > 1

import random, struct, socket, argparse
from random import getrandbits

# CLI arguments
parser = argparse.ArgumentParser(description='Returns a random IP address.')
group = parser.add_mutually_exclusive_group()
group.add_argument("-v4", "--ipv4", action="store_true")
group.add_argument("-v6", "--ipv6", action="store_true")
args = parser.parse_args()

# Function Defs
def rand_ipv4():
    return socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))

def rand_ipv6():
    return socket.inet_ntop(socket.AF_INET6, struct.pack('>QQ', getrandbits(64), getrandbits(64)))

if __name__ == "__main__":
    if args.ipv4:
        print(rand_ipv4())
    elif args.ipv6:
        print(rand_ipv6())
    else:
        print(rand_ipv4())
