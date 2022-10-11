import os
from time import sleep

def del_file(filenames):
    for filename in filenames:
                print("dirname : ",dirname ,"filename : ", filename)
                path_setting= dirname
                os.remove(dirname + "/" + filename);

def del_folder():
    for dirn in dirnames :
                if dirn != 'png' and path_setting != '' :
                    print("####"+path_setting+"/"+dirn)
                    try:
                        os.rmdir(path_setting+"/"+dirn)
                    except OSError as e: 
                        print ("Error: %s - %s." % (e.filename, e.strerror))



# for dirname, dirnames, filenames in os.walk('.'):
#     # print("dirname : ",dirname ,"dirnames : ",dirnames, "filenames : ",filenames)
#     # print path to all subdirectories first.
    
#     if dirname.find("portrait") != -1:

#         path_setting= ''
#         if dirname.find("png") != -1 :
#             continue
#         else :
#             # print(dirname)
#             del_file(filenames)
#             sleep()

#             for dirn in dirnames :
#                 if dirn != 'png' :
#                     try:
#                         os.rmdir(dirname+"/"+dirn)
#                     except OSError as e: 
#                         print ("Error: %s - %s." % (e.filename, e.strerror))


for dirname, dirnames, filenames in os.walk('.'):
    # print("dirname : ",dirname ,"dirnames : ",dirnames, "filenames : ",filenames)
    # print path to all subdirectories first.
    
    if dirname.find("portrait") != -1:
        # print("0:",dirname)

        path_setting= ''
        if dirname.find("png") != -1 :
            continue
        else :
            # print(dirname)
            for filename in filenames:
                # print("1:", filename)
                print("dirname : ",dirname ,"filename : ", filename)
                os.remove(dirname + "/" + filename)
                # print("del:dirname : ",dirname ,"filename : ", filename)

            try:
                os.rmdir(dirname)
            except OSError as e: 
                print ("Error: %s - %s." % (e.filename, e.strerror))
                # print("2:", dirname)




##Tree

#list (여기서 돌려야함)
#|--portrait
#|----c001(~n)
#|------png
#|--------01(~n)
#|------etc01(~n)


