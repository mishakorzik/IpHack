<img width="99.9%" src="https://raw.githubusercontent.com/mishakorzik/mishakorzik.menu.io/master/img/IpHack/20210822_200816.png"/>

<p align="center">
<a href="https://github.com/mishakorzik/IpHack"><img title="Version" src="https://img.shields.io/badge/Version-1.7-darkred?style=for-the-badge&logo="></a>
<a href="https://github.com/mishakorzik/IpHack/blob/main/LICENSE"><img title="License" src="https://img.shields.io/badge/Apache-License 2.0-red?style=for-the-badge&logo=apache"></a>
<a href=""><img title="Python" src="https://img.shields.io/badge/Made in-Ukraine-red?style=for-the-badge&logo=None"></a>
<a href="https://github.com/mishakorzik"><img title="Report" src="https://img.shields.io/badge/Copyring-2022-orange?style=for-the-badge&logo=github"></a>
<a href="https://github.com/mishakorzik"><img title="Autor" src="https://img.shields.io/badge/Author-mishakorzik-yellow?style=for-the-badge&logo=github"></a>

</p>

<p align="center">
• <a href="https://github.com/mishakorzik/IpHack/blob/main/LICENSE">License</a> 
• <a href="https://github.com/mishakorzik/IpHack/issues">Issues</a> 
• <a href="https://github.com/mishakorzik/IpHаck/projects">Project</a> 
• <a href="https://github.com/mishakorzik/IpHack/wiki">Wikipedia</a> •

</p>

> IpHack: is a tracking tool for both IP location and tracking testing.

---

**Track Location With Live Address And City in Termux**

> Я не несу ответственности за ваши действия. Скачивая программное обеспечение из этого репозитория, вы соглашаетесь с [лицензией](https://github.com/mishakorzik/IpHack/blob/main/LICENSE).

----
## New Features

**1) New Functions**
- Now you can find out in which country the person is.

**2) New Desing**
- Now a new design has been added and now it is more beautiful.

**3) More Information**
- Now you can learn more about the device via IP

**4) Detail Information**
- You can find out a lot of information about IP
-----
## Install

```bash
pip install iphack
```

**Ip Address**

```python
# ip address tracking
from iphack import ip
ip.address("ip") 

# domain ip address tracking
from iphack import ip
ip.domain("google.com")

# my ip address
from iphack import ip
ip.my()

# get domain ip
from iphack import ip
ip.domain("https://example.com")

```

**Inquiry**

```python
# anonymous request
from iphack import inquiry

# request from url, using tor & fake user-agent
>>> get = inquiry.get("https://api.ipify.org/") #method get
>>> print(get.text)
199.249.230.102
>>> 


post = inquiry.post("https://example.com") #method post
put = inquiry.put("https://example.com") #method put
delete = inquiry.delete("https://example.com") #method delete
head = inquiry.head("https://example.com") #method head

# inquiry logs
inquiry.debug() #enable log
inquiry.debug() #disable log
```

## Screenshot

**Without logs**
<img width="99.9%" src="https://raw.githubusercontent.com/mishakorzik/IpHack/main/IMG_20220822_110928.jpg"/>
**With logs**
<img width="99.9%" src="https://raw.githubusercontent.com/mishakorzik/IpHack/main/IMG_20220822_111039.jpg"/>

```
System   : Ubuntu 20.04 LTS
Terninal : Xfce4-Terminal
Desktop  : Xfce4
```
<img width="99.9%" src="https://raw.githubusercontent.com/mishakorzik/IpHack/main/Screenshot_2022-08-13_21-33-49.png"/>

## I recommend watching

1.<a href="https://github.com/mishakorzik/qiq">qiq - Useful batch installer</a>

2.<a href="https://github.com/mishakorzik/Gmail-Hack">Gmail-Hack - Easy email hacking</a>

3.<a href="https://github.com/mishakorzik/AdminHack">AdminHack - Hacking bad sites</a>

4.<a href="https://github.com/mishakorzik/Infect">Infect - Easy virus creation</a>

5.<a href="https://github.com/mishakorzik/Free-Proxy">Free-Proxy - Lots of free proxy servers</a>

6.<a href="https://github.com/mishakorzik/AllHackingTools">AllHackingTools - System for large hacking</a>

7.<a href="https://github.com/mishakorzik/Ultra-DDos">Ultra-DDos - Hing ddos bad sites</a>

## Supporters
[![Stargazers repo roster for @mishakorzik/IpHack](https://reporoster.com/stars/mishakorzik/IpHack)](https://github.com/mishakorzik/IpHack/stargazers)
[![Forkers repo roster for @mishakorzik/IpHack](https://reporoster.com/forks/mishakorzik/IpHack)](https://github.com/mishakorzik/IpHack/members)
