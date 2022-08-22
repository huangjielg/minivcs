
import os
import shutil
import tarfile
files = {}
BASE_DIR="/opt/synopsys"
TARGET_DIR="./opt"
BASE_DIR_LEN=len(BASE_DIR)


def create_tree(p):
    ps=p.split(os.sep)
    n=""
    for i in ps :
        n= n+os.sep+i
        #print(n)
        if os.path.islink(BASE_DIR+n):
            link_target = os.readlink(BASE_DIR+n)
            link_target_real = os.path.realpath(BASE_DIR+n)
           # print(n,link_target,link_target_real)
            if os.path.isdir(link_target_real):
                os.makedirs(TARGET_DIR+link_target_real[BASE_DIR_LEN:],exist_ok=True)
            try:
                os.symlink(link_target,TARGET_DIR+n)
            except:
                pass
            
        elif os.path.isdir(BASE_DIR+n):
            os.makedirs(TARGET_DIR+n,exist_ok=True)
        else:
            pass

        

with open("vcs_strace_a.txt") as f:
    for l in f.readlines():
        a = l.find('"'+BASE_DIR)
        b = l.find('"',a+1)
        s = os.path.normpath(l[a+1:b])
        if os.path.isfile(s):
            files[s] = os.stat(s)
#print(files)
a=0
n=0
for f,st in files.items():
    a=a+st.st_size
    n=n+1
    #break

print(n,a)    

# create directory tree
for f in files.keys():
    create_tree(os.path.relpath(f,start=BASE_DIR))
    
# copy files
for f in files.keys():
    rp = os.path.realpath(f)
    if rp.startswith(BASE_DIR):
        print(f,end=":")
        print(rp,end=":")
        dest=TARGET_DIR+rp[BASE_DIR_LEN:]
        print(dest)
        shutil.copy(f,dest)
    

