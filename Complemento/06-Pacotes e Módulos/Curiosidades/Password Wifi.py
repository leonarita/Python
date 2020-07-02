import subprocess

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors='backslashreplace').split('\n')
profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
print(profiles)
for i in profiles:

    try:
        r = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8', errors='backslashreplace').split('\n')
        r = [b.split(":")[1][1:-1] for b in r if "Key Content" in b]

        try:
            print("{:<30}|  {:<}".format(i, r[0]))
        except IndexError:
            print("{:<30}|  {:<}".format(i, ""))

    except subprocess.CalledProcessError:
        print("{:<30}|  {:<}".format(i, "ENCODING ERROR"))
