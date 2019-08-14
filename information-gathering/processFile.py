#coding:utf-8

import sys
import re

file1 = sys.argv[0]
file2 = sys.argv[1]
file3 = sys.argv[2]
file4 = sys.argv[3]
file5 = sys.argv[4]



# file1 = "/Users/stone/Desktop/BattleRedBlue/sumary/gitrepo/tools/result/subdomainbjut.edu.cn.txt"
# file2 = "/Users/stone/Desktop/BattleRedBlue/sumary/gitrepo/tools/result/tmp_sublist3rbjut.edu.cn.txt"
# file3 = "/Users/stone/Desktop/BattleRedBlue/sumary/gitrepo/tools/result/bjut.edu.cn.txt"
# file4 = "/Users/stone/Desktop/BattleRedBlue/sumary/gitrepo/tools/result/bjut.edu.cn_hosts.txt"
# file5 = "/Users/stone/Desktop/BattleRedBlue/sumary/gitrepo/tools/result/bjut.edu.cn_C_segment_sumary.txt"




def extractIp(filename):
    iplist = []
    f1 = open(filename,"rb")
    lines = f1.readlines()
    for line in lines:
        each = line.strip()
        ips=re.findall(r'(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d])',str(each),re.S)
        for ip in ips:
            iplist.append(ip)
    f1.close()
    return iplist

ip1 = extractIp(file1)
ip1.extend(extractIp(file2))
uniqIpList = list(set(ip1))

ip_C_dict = {}
for ip in uniqIpList:
    c_segment = ".".join(ip.split(".")[0:3])
    if ip_C_dict.has_key(c_segment):
        ip_C_dict[c_segment] = ip_C_dict[c_segment] + 1
    else:
        ip_C_dict[c_segment] = 1

## read the two files:
list_dict = {}
f1 = open(file1,"rb")
for line in f1.readlines():
    host =  line.strip().split()[0]
    ip = ",".join(line.strip().split()[1:])
    if not list_dict.has_key(host):
        list_dict[host] = ip

f2 = open(file2,"rb")
for line in f2.readlines():
    host =  line.strip().split()[0]
    ip = ",".join(line.strip().split()[1:])
    if not list_dict.has_key(host):
        list_dict[host] = ip

f2 = open(file3,"wb")
f3 = open(file4,"wb")
for key in list_dict.keys():

    f2.writelines(key+"##"+list_dict[key]+"\n")
    f3.writelines(key + "\n")

f3.close()
f2.close()

sumary_result = "##" * 10 + " C段统计分析 " + "##" * 10 + "\n"

sumary_result = sumary_result + "共有{0}个C段".format(len(ip_C_dict))

for ip in ip_C_dict.iterkeys():
    sumary_result = sumary_result + "C 段IP：" + ip + ".*\t 共有{0}个".format(ip_C_dict[ip])


f2 = open(file4,"wb")
f2.writelines(sumary_result)
f2.close()








