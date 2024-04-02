import json
import socket

import psutil
import requests


def readFile():
    with open('../resources/myData.json', 'r') as file:
        config_data = json.load(file)
        return config_data


def writeFile(config_data):
    with open('../resources/myData.json', 'w+') as file:
        json.dump(config_data, file, indent=6)


def getValue(key):
    data = readFile()
    try:
        return data[key]
    except KeyError as error:
        return None


def setValue(key, value):
    data = readFile()
    data[key] = value
    writeFile(data)


def get_local_ip():
    local_ip = socket.gethostbyname(socket.gethostname())
    setValue("CLIENT_LOCAL_IP", local_ip)
    return local_ip


def get_mac_address():
    mac_address = ""
    for interface in psutil.net_if_addrs().values():
        for addr in interface:
            if addr.family == psutil.AF_LINK:
                mac_address = addr.address
                setValue("MAC_ADDRESS", mac_address)
                return mac_address


def get_public_ip():
    public_ip = ""
    response = requests.get("https://api64.ipify.org?format=json")
    if response.status_code == 200:
        public_ip = response.json()["ip"]
        setValue("CLIENT_PUBLIC_IP", public_ip)
        return public_ip
    else:
        return None


def client_info():
    info_dict: dict = {"CLIENT_LOCAL_IP": get_local_ip(), "CLIENT_PUBLIC_IP": get_public_ip(),
                       "MAC_ADDRESS": get_mac_address()}
    return info_dict
