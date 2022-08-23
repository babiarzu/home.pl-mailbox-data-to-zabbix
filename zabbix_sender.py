import csv
import os

# zabbix sender path - use hard coded or env variable
PATH = "C:/your/path/zabbix_sender.exe"


def zabbix_sender():
    """
    Iterates through csv file, gathering email names, mailbox capacity
    and usage of that capacity. After that it calculates percentage usage
    of each mailbox, and sends that values to zabbix through cmd.
    """
    with open('C:/your/file/path.csv') as f:
        reader = csv.reader(f)
        arr = list(reader)

    # iterate through list from 1st position to ignore column names.
    for val in arr[1::]:
        email = val[0]
        used = int(val[4])
        size = int(val[5])
        pused = int(float(used) / float(size) * 100)

        # 127.0.0.1 - zabbix host
        command1 = r"%s -z 127.0.0.1 -s home.pl -k email -o [{\"{#EMAIL}\":\"%s\"}]" % (PATH, email)
        os.system(command1)
        command2 = "%s -z 127.0.0.1 -s home.pl -k email.[%s,used] -o %d" % (PATH, email, used)
        os.system(command2)
        command3 = "%s -z 127.0.0.1 -s home.pl -k email.[%s,size] -o %d" % (PATH, email, size)
        os.system(command3)
        command4 = "%s -z 127.0.0.1 -s home.pl -k email.[%s,pused] -o %d" % (PATH, email, pused)
        os.system(command4)
    os.remove('C:/your/file/path.csv')
