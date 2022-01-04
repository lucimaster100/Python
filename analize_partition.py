import sys
import os
import collections
import matplotlib.pyplot as plt
import itertools


count_limit=int(input("Set grouping limit for file count\ncount_limit="))
size_limit=int(input("Set grouping limit for file size(in GB)\nsize_limit="))

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

#group files that appear less than a number of times
newcount={}
for key, group in itertools.groupby(count, lambda k: 'Other files' if (count[k]<count_limit) else k):
     newcount[key] = sum([count[k] for k in list(group)])
print("file extention count:")
print(newcount)

#group files less than a given size in GB
newsize={}
for key, group in itertools.groupby(size, lambda k: 'Other files' if (size[k]<1000000000*size_limit) else k):
     newsize[key] = sum([size[k] for k in list(group)])
print("file extention size:")
print(newsize)
fig, ax = plt.subplots()
ax.pie(newcount.values(),labels=newcount.keys())
ax.axis=('equal')
plt.show()
fig, ax = plt.subplots()
ax.pie(newsize.values(),labels=newsize.keys())
ax.axis=('equal')
plt.show()
