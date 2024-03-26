"""
This project essentially just modifies the product.json file of vscodium on windows and linux to make Microsoft think it's 
normal VSCode and allow VSCode proprietary extensions. This basically makes VSCodium just as useful as VSCode, but better since there is no data collection. 
The only drawback is that VSCode extensions aren't open source. This doesn't have macos support because of 4 reasons:
1. If you choose to use a mac for programming, WHAT IS WRONG WITH YOU?!?
2. I do not own a mac and NEVER will.
3. If you choose to use a mac for literally anything, you are an "Isheep".
4. Just please PLEASE sell your mac to another Isheep and get a PC.

If you are a Isheep that wants to stay an Isheep for some reason, here is a guide to do this yourself, however, since I don't own a mac :) I havn't tested this.
This is basically what I did for windows and linux. If one of you Isheep make add support for mac yourself, please let me know so I can add it to the main repo.
Or you know, just sell your mac, PLEASE.
https://www.flypenguin.de/2023/02/26/use-vscodium-with-microsofts-proprietary-marketplace/

"""

import platform
import getpass
import json
import os

if platform.system() == "Windows":
    print("Windows")
    usrnm = input('please enter your windows username or leave this blank to detect your username automatically > ')

    if usrnm == '':
        usrnm = getpass.getuser()
    # print (usrnm)        
    if os.path.exists(f'C:\\Users\\{usrnm}\\AppData\\Local\\Programs\\VSCodium\\resources\\app\\product.json'):
        
        with open(f"C:\\Users\\{usrnm}\\AppData\\Local\\Programs\\VSCodium\\resources\\app\\product.json", 'r') as f:
            pruductjson = json.loads(f.read())
        print(pruductjson['extensionsGallery'])
        with open(f"C:\\Users\\{usrnm}\\AppData\\Local\\Programs\\VSCodium\\resources\\app\\product.json", 'w') as f:
            pruductjson['extensionsGallery']['cacheUrl'] = "https://marketplace.visualstudio.com/_apis/public/gallery"
            pruductjson['extensionsGallery']['serviceUrl'] = "https://marketplace.visualstudio.com/_apis/public/gallery"
            pruductjson['extensionsGallery']['itemUrl'] = "https://marketplace.visualstudio.com/items"
            f.write(json.dumps(pruductjson))
    else:
        print (f'Products.json file does not exist in dir "C:\\Users\\{usrnm}\\AppData\\Local\\Programs\\VSCodium\\resources\\app\\product.json"')

elif platform.system() == "Linux":
    print("Linux")
    #usrnm = input ('please enter your username, you can find it in your /home dir > ' )#getpass.getuser()

    if os.path.exists(f'/usr/share/codium/resources/app/product.json'):
        
        with open(f"/usr/share/codium/resources/app/product.json", 'r') as f:
            pruductjson = json.loads(f.read())
        print(pruductjson['extensionsGallery'])
        with open(f"/usr/share/codium/resources/app/product.json", 'w') as f:
            pruductjson['extensionsGallery']['cacheUrl'] = "https://marketplace.visualstudio.com/_apis/public/gallery"
            pruductjson['extensionsGallery']['serviceUrl'] = "https://marketplace.visualstudio.com/_apis/public/gallery"
            pruductjson['extensionsGallery']['itemUrl'] = "https://marketplace.visualstudio.com/items"
            f.write(json.dumps(pruductjson))
    else:
        print (f'Products.json file does not exist in dir "/usr/share/codium/resources/app/product.json", if you uninstalled codium with snap, uninstall it and reinstall it using sudo apt.')


else:
    print("Mac")
    print ('As I do not own a mac (and never plan to), you can not use this on a mac.')


