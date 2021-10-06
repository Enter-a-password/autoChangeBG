try:
    from os import remove, getenv
    input("Press enter to continue ChangeBG uninstaller")

    username = getenv("username")
    onedrive = getenv("onedrive")
    shellpath = f"C:\\Users\\{username}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"

    # Remove startup file
    try:
        remove(f'{shellpath}\\ChangeBG.pyw')
    except FileNotFoundError:
        print("Unable to remove automatic startup agent; Manually remove from\n", shellpath)
    

    rfolder = input("Remove GBWallpapers folder? y/n\nChoice: ")
    rfolder.lower()

    if rfolder == 'y' or rfolder == 'yes':
        from shutil import rmtree
        try:
            rmtree(f"{onedrive}\\Other\\Documents\\BGWallpapers\\")
        except FileNotFoundError:
            input("Unable to find BGWallpapers folder")
            
        # Remove shortcut
        try:
            remove(f'{onedrive}\\Other\\Desktop\\BGWallpapers.lnk')
        except:
            pass

    input("Uninstaller finished")
    exit()
except Exception as e:
    print("Unable to continue uninstaller")
    input('Error: ', e)