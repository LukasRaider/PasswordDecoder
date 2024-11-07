import subprocess

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace")
lines = data.split('\n')
profiles = [line.split(":")[1].strip() for line in lines if "All User Profile" in line]


for profile in profiles:
    try:
        result = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear']).decode('utf-8', errors="backslashreplace")
        key_lines = result.split('\n')
        key_content = [line.split(":")[1].strip() for line in key_lines if "Key Content" in line]

        if key_content:
            print("{:<30}| {:<}".format(profile, key_content[0]))
        else:
            print("{:<30}| {:<}".format(profile, "N/A"))
    except subprocess.CalledProcessError:
        print("{:<30}| {:<}".format(profile, "CHYBA DEKÓDOVÁNÍ"))

input("Stiskněte libovolnou klávesu pro ukončení...")
