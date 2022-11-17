from home import home_downloader
from zabbix_sender import zabbix_sender

if __name__ == "__main__":
    home_downloader()
    zabbix_sender()
