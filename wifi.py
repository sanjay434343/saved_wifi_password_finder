import subprocess

def get_wifi_profiles():
    try:
        result = subprocess.run(['netsh', 'wlan', 'show', 'profiles'], capture_output=True, text=True, check=True)
        output = result.stdout
        profile_names = [line.split(":")[1].strip() for line in output.split("\n") if "All User Profile" in line]
        return profile_names
    except subprocess.CalledProcessError:
        return []

def get_wifi_password(profile_name):
    try:
        result = subprocess.run(['netsh', 'wlan', 'show', 'profile', profile_name, 'key=clear'], capture_output=True, text=True, check=True)
        output = result.stdout
        password_index = output.find("Key Content")
        if password_index != -1:
            password = output[password_index+14:].split('\n')[0].strip()
            return password
        else:
            return "Password not found."
    except subprocess.CalledProcessError:
        return "Error: Wi-Fi profile not found."

# Get all Wi-Fi profiles
wifi_profiles = get_wifi_profiles()

# Get passwords for each Wi-Fi profile
for profile in wifi_profiles:
    password = get_wifi_password(profile)
    print(f"Wi-Fi profile: {profile}, Password: {password}")
    