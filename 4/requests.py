#http://www.pythonchallenge.com/pc/def/linkedlist.html
import requests

first_url ='http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345';	

response = requests.get(first_url);


for i in range(1,400) :
	url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
	
	firstIndex = response.text.find('next nothing is ')
	lastIndex = len(response.text)

	param = response.text[firstIndex+16:lastIndex]
	print(response.text)
	print(param)
	url+=param
	response = requests.get(url);

