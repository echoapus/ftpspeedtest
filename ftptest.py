from ftplib import FTP
import time

def download_file_ftp(ftp_host, ftp_username, ftp_password, remote_file, local_file):
    start_time = time.time()  #start_time

    with FTP(ftp_host) as ftp:
        ftp.login(user=ftp_username, passwd=ftp_password)
        with open(local_file, 'wb') as file:
            ftp.retrbinary('RETR ' + remote_file, file.write)

    end_time = time.time()  #End_time
    download_time = end_time - start_time  #Time

    return download_time

# 使用範例
ftp_host = 'ftp.speed.hinet.net'  # FTP Server
ftp_username = 'ftp'  # user
ftp_password = 'ftp'  # password
remote_file = '/test_400m.zip'  #File
local_file = '/tmp/test_400m.zip'  #location

time_taken = download_file_ftp(ftp_host, ftp_username, ftp_password, remote_file, local_file)
print(f"Total time: {time_taken} seconds")
