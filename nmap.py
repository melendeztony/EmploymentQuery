import os
from ip_address import*


def get_nmap(options, ip):
    command = "nmap " + options + " " + ip
    process = os.popen(command)
    results = str(process.read())
    return results


