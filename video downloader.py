import os
import io
import subprocess

# Programm to download videos or streams (get that by filtering in the network menu of chromes site inspector, may need a reload. m3u is a good keyword for filtering)
# in line 57 you can change audio and video codec settings (mp4, aac, etc.), currently .mkv is set

# initializing
url = []
url_n = []
names_with_spaces = []
names_with_drop = []
name = []

l = 0
o = 0
i = 0
# the path to this folder
p = os.getcwd()

# Grabbing the URL
with open(p+'\\urls.txt') as u:       # file path can be changed
    url_n = u.readlines()
    u.close()

# Grabbing the title
with open(p+'\\names.txt') as n:      # file path can be changed
    names_with_spaces = n.readlines()
    n.close()
    
# removing spaces and returns from the txt, else there are errors
while l < len(names_with_spaces):
    x = names_with_spaces[l].replace(' ','_')
    names_with_drop.append(x)
    x = names_with_drop[l].replace('\n','')
    name.append(x)
    l = l + 1

# removing the return of the txt
while o < len(url_n):
    x = url_n[o].replace('\n','')
    url.append(x)
    o = o + 1    

# Just for Control Purposes, not needed  
# print('with spaces and returns')  
# print (names_with_spaces)
# print ('no spaces and returns')
# print (name)





# grabbing and converting the video to the desired format at the desired place
def grab_video(source,output):
    command = p+"\\ffmpeg\\bin\\ffmpeg.exe -i {} -c copy {}.mkv".format(source,output)      # the video format can be changed, same for destination
    subprocess.call(command, shell=True)

# loop to download multiple files
while i < len(url):
    grab_video(url[i],name[i])
    i=i+1
