# TTCscript
A short script that replaces Tamriel Trade Centre .exe file with a python solution


Instructions: 
If you don't have python, get it from windows store, and if the script does not update the price table correctly, and reports errors about missing modules, open windows terminal (cmd) and type 'python pip install whatevermodulenameismissing'

1. Paste the script into C:\Users\USERNAME\Documents\Elder Scrolls Online\live\AddOns\TamrielTradeCentre
2. Create a shortcut with
C:\Windows\System32\cmd.exe /k python "C:\Users\USERNAME\Documents\Elder Scrolls Online\live\AddOns\TamrielTradeCentre\get.py" "eu" && exit
on your desktop or wherever you like, if you're playing on NA, replace "eu" with "us"
3. Enjoy, the script should automatically download and unzip the price table every time its run
