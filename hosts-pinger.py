import os
import json
from utils.list_pinger import *

def hosts_extractor(server_list):
    target_dic = server_list["ips"]
    target_servers = list(target_dic.values())
    target_server_flat = []
    for i in target_servers:
        if isinstance(i, list):
            for m in i:
                 target_server_flat.append(m)
        else:
            target_server_flat.append(i)
    target_servers = target_server_flat	
    return target_servers    

list_files = os.listdir()
ping_lists = []

for i in list_files:
    if i.find('.json') != -1:
        ping_lists.append(i)

if len(ping_lists) == 0:
    print('Sorry, no list for check')
    exit()

elif len(ping_lists) == 1:
    print('Ready to call extractor')

else:
    n = 1
    for i in ping_lists:
        num = str(n)
        print(num + ' ' + i)
        n = n + 1
    n = n - 1
    file_to_process = input("Please, choose source file. Input number:")
    if file_to_process.isnumeric() == False:
        print("Wrong input, please repeat")
        exit()
    else:
        if int(file_to_process) > n or int(file_to_process) < 1:
            print("Wrong input, please repeat")
            exit()
        else:
            file_num = int(file_to_process) - 1
            file_json = ping_lists[file_num]
          
proto_server_list = (open(file_json, 'r'))
server_list = json.load(proto_server_list)

servers_for_ping = (hosts_extractor(server_list))

for i in servers_for_ping:
	print("for " + i + " result is "  + ping(i))
