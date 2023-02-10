import psutil
import time


def check_blocks():
    # Lấy thông tin về tất cả các block trên hệ thống
    partitions = psutil.disk_partitions()

    # Duyệt qua tất cả các block
    for partition in partitions:
        # Lấy thông tin về block
        block_info = psutil.disk_io_counters(perdisk=True)[partition.device]

        # In ra thông tin về block
        print("Device:", partition.device)
        print("Read bytes:", block_info.read_bytes)
        print("Write bytes:", block_info.write_bytes)
        print("----------------------------------------")


# Thực thi hàm check_blocks mỗi 5 giây
while True:
    check_blocks()
    time.sleep(5)
