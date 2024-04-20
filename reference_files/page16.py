import os
folder_name="C:\\Users\\tupti\\OneDrive\\Desktop\\new Lang\\Sem4\\SwiftSynk_PythonProject-1\\App\\test1"
print(os.listdir(folder_name))

for i in os.listdir(folder_name):
    print(i)
    if(os.path.isfile(folder_name+"\\"+i)):
        print(i, "file")
    if(os.path.isdir(i)):
        print(i, "folder")
