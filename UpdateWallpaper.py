import urllib2, re, httplib, urllib, ctypes, os, sys

#figure out where this scriot it on your machine             
pathname = os.path.dirname(sys.argv[0])        

#setup custom header before requesting the website
httplib.HTTPConnection.debuglevel = 1  
request = urllib2.Request('https://www.reddit.com/r/wallpaper/top')
opener = urllib2.build_opener()
request.add_header('User-Agent',
     'WallpaperMan')

#the html of the page you requested
feeddata = opener.open(request).read()

#look in the feeddata for the source of the top ranked wallpaper
regex = '<a class="thumbnail may-blank outbound " href=(.+?)>'
pattern = re.compile(regex)
ranks = re.findall(pattern, feeddata)
topPic = ranks[0]
source = topPic.split()
picture = source[0]
Newpicture = picture.lstrip('"')
print "Source: "+ Newpicture

#go download the image
testfile =urllib.URLopener()
testfile.retrieve(Newpicture,"piccy.jpg")

#build the full path to the downloaded picture
newWall = os.path.join(pathname,"piccy.jpg")

#set the wallpaper
SPI_SETDESKWALLPAPER = 20 
ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, newWall , 0)




    
