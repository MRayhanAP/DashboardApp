import psutil

drives = ['C:\\', 'D:\\', 'E:\\', 'G:\\', ]
obj_drives = []

def GetDriveSpace():
    print("-GETTING HARD DRIVE SPACE")

    disk_c = psutil.disk_usage('C:\\')
    disk_c_gb = [int(disk_c.total / (1024.0 ** 3)), int(disk_c.used / (1024.0 ** 3)), int(disk_c.free / (1024.0 ** 3))]
    disk_d = psutil.disk_usage('C:\\')
    disk_d_gb = [int(disk_d.total / (1024.0 ** 3)), int(disk_d.used / (1024.0 ** 3)), int(disk_d.free / (1024.0 ** 3))]

    data_return = [disk_c, disk_d, disk_c_gb, disk_d_gb]

    return data_return