import os

f = open("C:\\Users\VICTUS\Algoritma-Pemrograman-TI-B-2026\pertemuan12\welcome.txt")
print(f.readline())
f.close()

#TESTING MORE




with open("myfile.txt",'w') as h:
   h.write("Somebody once told me")

os.rmdir("tes")