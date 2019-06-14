#coding:utf-8

import requests

def run(url):
    result = ""
    result += git(url) or ""
    result += svn(url) or ""
    if result:
        return result
    else:
        return False

def git(url):
   req = requests.get(url + "/.git")
   if req.status_code == 200:
        return ".git found in %s" % url
   else:
        return False

def svn(url):
    req = requests.get(url + "/.svn")
    if req.status_code == 200:
        return ".svn found in %s" % url
    else:
        return False

if __name__ == "__main__":
    print(run("http://127.0.0.1"))
