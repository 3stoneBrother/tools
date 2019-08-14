#/bin/bash

path=`pwd`
domain=$1

cd ./subdomain_collection/subDomainsBrute
python subDomainsBrute.py  $domain --full -o ./../../result/subdomain$domain.txt


cd $path
cd ./subdomain_collection/Sublist3r
python sublist3r.py -d $domain -o ./../../result/sublist3r$domain.txt


for i in `cat ./../../result/sublist3r$domain.txt`
do
  	ip=`ping -c 1 $i | grep "icmp_seq=0" | cut -d " " -f4 | cut -d ":" -f1`
  	echo "$i $ip" >> ./../../result/tmp_sublist3r$domain.txt
done


cat ./../../result/subdomain$domain.txt ./../../result/tmp_sublist3r$domain.txt | sort | uniq > ./../../result/$domain.txt

# file1 = "/Users/stone/Desktop/BattleRedBlue/sumary/gitrepo/tools/result/subdomainbjut.edu.cn.txt"
# file2 = "/Users/stone/Desktop/BattleRedBlue/sumary/gitrepo/tools/result/tmp_sublist3rbjut.edu.cn.txt"
# file3 = "/Users/stone/Desktop/BattleRedBlue/sumary/gitrepo/tools/result/bjut.edu.cn.txt"
# file4 = "/Users/stone/Desktop/BattleRedBlue/sumary/gitrepo/tools/result/bjut.edu.cn_hosts.txt"
# file4 = "/Users/stone/Desktop/BattleRedBlue/sumary/gitrepo/tools/result/bjut.edu.cn_C_segment_sumary.txt"

cd $path

basePath = "./result/"

python processFile.py $basePathsubdomain$domain.txt "$basePath""tmp_sublist3r""$domain.txt" $basePath$domain.txt $basePath$domain_hosts.txt $basePath$domain_C_segment_sumary.txt


nmap -Pn -iL ./result/$domain_hosts.txt -oA ./result/$domainNmap


hostfile = `$basePath$domain_hosts.txt`
#python ./WharWeb/whatweb --no-errors --url-prefix http:// -i $hostfile --log-brief=$basePath$domain_whatweb.txt