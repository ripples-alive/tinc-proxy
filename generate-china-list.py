#!/usr/bin/env python
# coding:utf-8

import re
import math
import urllib2


def fetch_ip_data():
    # fetch data from apnic
    url = r'http://ftp.apnic.net/apnic/stats/apnic/delegated-apnic-latest'
    data = urllib2.urlopen(url).read()
    cn_regex = re.compile(r'apnic\|cn\|ipv4\|[0-9\.]+\|[0-9]+\|[0-9]+\|a.*',
                          re.IGNORECASE)
    cn_data = cn_regex.findall(data)
    ip_data = []

    for item in cn_data:
        unit_items = item.split('|')
        starting_ip = unit_items[3]
        num_ip = int(unit_items[4])

        imask = 0xffffffff ^ (num_ip - 1)
        #convert to string
        imask = hex(imask)[2:]
        mask = [0] * 4
        mask[0] = imask[0:2]
        mask[1] = imask[2:4]
        mask[2] = imask[4:6]
        mask[3] = imask[6:8]

        #convert str to int
        mask = [int(i, 16) for i in mask]
        mask = "%d.%d.%d.%d" % tuple(mask)

        #mask in *nix format
        mask2 = 32 - int(math.log(num_ip, 2))

        ip_data.append((starting_ip, mask, mask2))

    return ip_data


ip_data = fetch_ip_data()

print '#!/bin/bash'
for ip, mask, mask_len in ip_data:
    print 'ipset add $SET_NAME %s/%d' % (ip, mask_len)
