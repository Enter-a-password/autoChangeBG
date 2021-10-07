try:
    print("ChangeBG installer")
    print("Please acknowledge the fact that this is to only be used in the Westada School district")
    input("Press enter to continue installation")
    from os import getenv
    from os.path import isdir
    from ctypes import windll
    from subprocess import Popen

    username = getenv("username")
    onedrive = getenv("onedrive")
    shellpath = f"C:\\Users\\{username}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"

    if onedrive == 'None':
        input("Unable to continue installation; onedrive has not been connected")
        exit(404)


    # If the directory to the Wallpapers folder doesn't exist, create one
    if not isdir(f'{onedrive}\\Other\\Documents\\BGWallpapers'):
        from os import makedirs
        makedirs(f'{onedrive}\\Other\\Documents\\BGWallpapers')

    # Open and write code from file
    with open("assets/changeBackground.txt", "r") as f:
        code = f.read()
        f.close()
    with open(f'{shellpath}\changeBG.pyw', 'w') as f:
        f.write(code)
        f.close

    # Copy Image
    with open(f'assets/wallpaper.jpeg', 'br') as f:
        exwallpaper = f.read()
        f.close()
    with open(f"{onedrive}\\Other\\Documents\\BGWallpapers\\wallpaper.jpeg", 'bw') as f:
        f.write(exwallpaper)
        f.close()
    
    # Open folder
    Popen(f'explorer /select, "{onedrive}\\Other\\Documents\\BGWallpapers\\wallpaper.jpeg"')

    user32 = windll.user32
    screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    print(f"\n\nMake sure to have an image that is the same resolution as your display\nYour display size: {screensize}")
    

    input("Installer is finished")
    exit()

except Exception as e:
    print("Unable to Continue installer")
    input('Error: ', e)
