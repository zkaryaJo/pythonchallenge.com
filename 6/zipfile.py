#http://www.pythonchallenge.com/pc/def/channel.html -> channel.zip
import zipfile

prefix = './channel/'
lastfix = '.txt'
num = '90052'

msg_firstIndex = 0
msg_lastIndex = 0
sum = 90052
allComments =""
zf = zipfile.ZipFile("channel.zip")

for i in range(909) :
	fileName = prefix+num+lastfix;

	allComments += zf.getinfo(num+lastfix).comment


	#file read and save string to str
	with open(fileName,'rt') as file:
		str = file.readlines()
		
	#convert list to string
	rtnStr = "".join(str)
	#print(rtnStr)
	
	#handle str to num
	msg_firstIndex = rtnStr.find('Next nothing is ')+16 
	msg_lastIndex = len(rtnStr)
	num = rtnStr[msg_firstIndex:msg_lastIndex]
	if i!=908 :
		sum+=int(num)

#print sum
print allComments
