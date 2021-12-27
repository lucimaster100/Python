import sys
import os
import collections
import matplotlib.pyplot as plt

drive=sys.argv[1]
ndirs=0
nfiles=0
count = collections.Counter()
size=collections.Counter()

for (root,directories,files) in os.walk(drive+":\\"):
    ndirs+=len(directories)
    nfiles+=len(files)
    for fileName in files:
        full_fileName = os.path.join(root,fileName)
        name,ext = os.path.splitext(fileName)
        count[ext]+=1
        size[ext]+=os.path.getsize(full_fileName)
print("directories: " + f"{ndirs}" +" files: " + f"{nfiles}")
fig1, ax1 = plt.subplots()
ax1.pie(count.values(),labels=count.keys())
ax1.axis=('equal')
plt.show()
