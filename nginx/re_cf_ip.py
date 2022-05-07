import requests
r = requests.get('https://www.cloudflare.com/ips-v4').text
w = requests.get('https://www.cloudflare.com/ips-v6').text
with open('conf/cf-connect-ip.conf',encoding='utf-8',mode='w') as confs:
    for line in (r+'\n'+w).split("\n"):
        print(line)
        confs.write('set_real_ip_from {ips};\n'.format(ips=line))
