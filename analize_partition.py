import sys
import os
import collections
import matplotlib.pyplot as plt
import itertools

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

#group files that appear less than 150 times
newcount={}
for key, group in itertools.groupby(count, lambda k: 'Other files' if (count[k]<500) else k):
     newcount[key] = sum([count[k] for k in list(group)])
print("file extention count:")
print(count)

#group files less than 10GB
newsize={}
for key, group in itertools.groupby(size, lambda k: 'Other files' if (size[k]<10000000000) else k):
     newsize[key] = sum([size[k] for k in list(group)])
print("file extention size:")
print(size)
fig, ax = plt.subplots()
ax.pie(newcount.values(),labels=newcount.keys())
ax.axis=('equal')
plt.show()
fig, ax = plt.subplots()
ax.pie(newsize.values(),labels=newsize.keys())
ax.axis=('equal')
plt.show()
