import os

name = input("nome do atalho?\n")
path = "/home/dcr/.local/share/applications/" + name + ".desktop"
print(name)
f = open(path, "w")
f.write("[Desktop Entry]\n")
f.write("Type=Application\n")
f.write("Name=" + name + "\n")
ex = input("path to executable?\n")
f.write("Exec=" + ex + "\n")
icon = input("path to Icon?\n")
if (icon != ""):
	f.write("Icon=" + icon + "\n")
f.write("Terminal = false")
f.close()

os.system("chmod +x " + path)

