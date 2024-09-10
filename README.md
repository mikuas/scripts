#!/bin/bash


~~~bash

locale
sudo nano /etc/locale.gen
# 重新生成语言环境
sudo locale-gen

sudo nano /etc/default/locale
# 写入 >
LANG=en_US.UTF-8
LC_MESSAGES=en_US.UTF-8



##### 中文
sudo apt update
sudo apt install language-pack-zh-hans
sudo update-locale LANG=zh_CN.UTF-8

##### 英文
sudo apt-get update
sudo apt-get install locales
sudo dpkg-reconfigure locales
sudo update-locale LANG=en_US.UTF-8

~~~

##### if判断

~~~bash

if [ "$#" -ne 2 ]; then
  echo "Usage: $0 <targetIp> <routeIP>"
  exit 1
fi

# 使用默认值 传了使用传递的参数,没有则使用value
element=${1:value}

# 判断传递值的个数
-lt 少于 -gt 多于
~~~

* $#:

    这是一个特殊变量，表示传递给脚本的参数数量。

* -ne:

    这是一个数值比较运算符，表示 "not equal"（不等于）。

* [ "$#" -ne 2 ]:

    这是一个条件测试，检查传递给脚本的参数数量是否不等于 2。

* then:

    如果条件 [ "$#" -ne 2 ] 为真（即参数数量不等于 2），则执行 * then 后的命令。


* echo "Usage: $0 <targetIp> <routeIP>":

    这行命令会输出用法提示，其中 $0 是脚本的名称。

* exit 1:

    退出脚本并返回状态码 1，表示有错误发生。

* fi:

    结束 if 语句块。


------------------------------------

##### 检查是否为根用户:

~~~bash

if [ "$EUID" -ne 0 ]; then
  echo "Please run as root"
  exit 1
fi

# 这里，$EUID 是一个特殊变量，表示当前用户的 ID。根用户的 ID 是 0。
~~~

-------------------------------------------

##### 检查文件是否存在:

~~~bash

if [ -f "$filename" ]; then
  echo "File exists"
else
  echo "File does not exist"
fi

~~~