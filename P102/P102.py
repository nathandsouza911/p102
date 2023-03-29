import os
import shutil

from_dir="C:/Users/Nikhil/Downloads"
to_dir="G:/NATHAN"

list_of_files=os.listdir(from_dir)
print(list_of_files)
for i in list_of_files:
    root,ext=os.path.splitext(i)
    if ext=="":
        continue
    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif',".mcworld",".mcaddon",".mcpack",".pptx",".PNG",".mp4",".zip",'.pdf',".txt",".exe",".xlsx",  '.doc', '.docx']:
        path1 = from_dir+"/"+i
        path2=to_dir+"/"+ext
        path3=to_dir+"/"+ext+"/"+i
        if os.path.exists(path2):
            print("moving"+i+"to--------")
            shutil.move(path1,path3)
        else: 
            os.mkdir(path2)    
            print("moving"+i+"to--------")
            shutil.move(path1,path3)