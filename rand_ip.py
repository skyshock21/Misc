#!/usr/bin/env python
#
# rand_ip.py
# A script to output random IP addresses
# example usage:
# python rand_int.py -n 10 -v6
# outputs 10 random IPv6 addresses

import random, struct, socket, argparse, sys
from random import getrandbits

# CLI arguments
parser = argparse.ArgumentParser(description='Returns a random IP address.')
group = parser.add_mutually_exclusive_group()
group.add_argument("-v4", "--ipv4", action="store_true")
group.add_argument("-v6", "--ipv6", action="store_true")
parser.add_argument("-n", "--number", type=int, help="Number of IPs to output")
args = parser.parse_args()

# Function Defs
def rand_ipv4():
    return socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))

def rand_ipv6():
    return socket.inet_ntop(socket.AF_INET6, struct.pack('>QQ', getrandbits(64), getrandbits(64)))

# Main logic - Check if no arguments were passed, and output an ipv4 address (default)
# if a value was specified as a flag -n, check if -v6 flag also passed and output -v6 format n times
# if a value was specified as a flag -n, and -v6 flag not set, output -v4 format, n times
# if no value was specified as -n, check if -v4 or -v6 flag were specified and output in that
# respective format
# if no flags specified, output a single v4 address (default) 
if __name__ == "__main__":
    if not len(sys.argv) > 1:
        print(rand_ipv4())
    elif args.number==0:
        print("-n passed a zero, bailing")
        exit()
    elif args.number:
        if args.ipv6:
            for i in range(args.number):
                print(rand_ipv6())
        else:
            for i in range(args.number):
                print(rand_ipv4())
    elif args.ipv6:
        print(rand_ipv6())
    elif args.ipv4:
        print(rand_ipv4())
    else:
        print(rand_ipv4())

