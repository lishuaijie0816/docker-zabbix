#/bin/bash

file=/usr/lib/zabbix/alertscripts/SendMail_Zabbix.log

echo `date '+%Y-%m-%d %H:%M:%S'` >> ${file}
echo "发送通知：$1" >> ${file}
echo "$2\n$3" >> ${file}
/usr/bin/python /usr/lib/zabbix/alertscripts/SendMail.py "$1" "$2" "$3" >> ${file}

