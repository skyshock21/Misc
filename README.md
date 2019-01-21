# Output Random IP address

RandIP.py allows you to output a random IP address in either IPv4 or IPv6 format.  It can serve as a library to be imported as well.  

## Run Application

In the directory where the script is stored run:

```
python rand_ip.py
```

By default it will output an IPv4 address, and the flag -v4 will also output an IPv4 address.  If you want an IPv6 address, type:

```
python rand_ip.py -v6
```

If you wish to specify multiple addresses for output, use the -n flag and pass in an integer value for the number of addresses you wish to output (default is ipv4):

```
python rand_ip.py -n 10
python rand_ip.py -v6 -n 10
python rand_ip.py -v4 -n18
```

If running properly you should see random IP addresses returned in the format you specified.
