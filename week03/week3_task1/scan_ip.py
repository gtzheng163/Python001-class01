import subprocess,os
import fire
import socket
import threading
from queue import Queue
from concurrent.futures import ThreadPoolExecutor
from ipaddress import ip_address

success_ports = []
ip_used=[]
lock = threading.Lock()

def pg_ip(ip01):

    """
    ping单个ip地址，打印出有效的ip地址
    """
    
    try:
        res = subprocess.call('ping -n 2 -w 5 %s' % ip01, stdout=subprocess.PIPE)  # linux 系统将 '-n' 替换成 '-c'
        #t=f"ping {ip01}"
        # res = subprocess.run(["ping",ip01, "-t", "2"] , capture_output=True)  # linux 系统将 '-n' 替换成 '-c'
        # 打印运行结果
        print(ip01, True if res == 0 else False)
       
        if res == 0:ip_used.append(ip01)
                                
    except Exception as e:
       
       print(e)
  
def tcp_link(ip_port_tuple):

    """
    用socket连接ip地址及端口，参数 ip_port_tuple 为一个元祖
    """
    if lock.acquire():
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # connect to remote host
        try:
            s.connect(ip_port_tuple)
            port_ok = ip_port_tuple[1]
            success_ports.append(port_ok)  
            
        except Exception as e:
            print('Error:', e)
        finally:
            s.close()
            lock.release()

def ping_func(n, f, ip):

    """
    把ip地址格式标准化，用map方式加入线程池
    """
    
    if f == 'ping':

        #two parts
        if "-" in ip:
            seed=[]
            ip_start, ip_end = ip.split('-')
            ip_start = ip_address(ip_start)
            ip_end = ip_address(ip_end)
            while ip_start <= ip_end:
                #IP_QUEUE.put(str(ip_start))
                seed.append(str(ip_start))
                ip_start += 1
            '''
            k=start_ip.split(".")
            start_last_num = k[-1]
            print(start_last_num)
            h=stop_ip.split('.')
            stop_last_num = h[-1]
            before = ".".join(k[:3])
            print(stop_last_num,before)
            seed = [before + '.' + str(num) for num in range(int(start_last_num), int(stop_last_num)+1)]
            #print(seed)
        '''
        else:
            seed=[]
            seed.append(ip)
            #print(seed)

        with ThreadPoolExecutor(n) as executor:
            executor.map(pg_ip, seed)
        

    elif f == 'tcp':
        seed = [(ip, port) for port in range(0, 1024)]
        with ThreadPoolExecutor(n) as executor:
            executor.map(tcp_link, seed)
        print(f'IP地址{ip}的所有开放端口是：{success_ports}\n')
    else:
        print("You can only call 'ping' or 'tcp' function!")

fire.Fire(ping_func)
print(ip_used)