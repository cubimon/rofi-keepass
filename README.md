# Rofi-keepass

Get any password from rofi by binding `find_password.py` to any key.
First you need the python dependencies `pyperclip` for clipboard access, `rofi` to open up rofi and `pykeepass`to open the kbdx file.
The kbdx location is specified in `general.py` and the password must be in the current working directory in a file named `.password`.
To avoid long decryption time before showing up rofi `update_entry_cache.py` should be called whenever the kbdx file changes to build up the entries that rofi displays.

