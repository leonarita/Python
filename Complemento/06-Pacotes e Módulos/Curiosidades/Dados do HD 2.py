import shutil

path = ""
stat = shutil.disk_usage(path)

print("Disk usage statistics: ")
print(stat)