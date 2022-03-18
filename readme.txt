This Program is supposed to help you download videos or livestreams more easily, especially when the media isn't embedded directly in the sourcecode and is only streamed in small segments (xhr, etc.)

How to use the programm
1. find a video you want to download
2. open the inspect page via right click, there open the network menu
3. filter for stuff with 'm3u' in it
4. if you found something, right click it and copy the link to it
5. paste the copied link in the url.txt
6. set a desired name in the name.txt in the same line as the url in the other file
7. execute the programm 'video downloader' (Visual Studio Code, IDLE, etc.)
8. download should start, the file is saved by default in the same folder as the programm

If you have multiple downloads only put one entry in each line and keep an eye open to match the name and url to each others line.
There is only one Download at the same time, you could of course start multiple instances with different content of the url and name file, but that is up to you.
Take note that streams will only be recorded/saved from where you started the programm, as with all cmd things you can stop the programm with ctrl + c.

I tested the programm with Python 3.10, but it should work with other versions as well.
Needs to be executed on Windows, since it uses CMD.

I'm a total newb concerning programming and this is mostly a mashup of my measly knowledge and things i found on stackoverflow (like a real programmer ;)).
So if you want to make improvements to the programm, feel free to do so.

Also I'm not responsible for what you do with this programm, so adhere to your local laws and stuff.