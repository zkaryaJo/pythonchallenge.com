# http://www.pythonchallenge.com/pc/def/peak.html
import requests
import pickle	#pickle is 

url = 'http://www.pythonchallenge.com/pc/def/banner.p'

res = requests.get(url);

data = pickle.loads(res.text); # pickle load() vs loads()

print(data)

for line in data :		#per line
	result = ""
	for i in range(0, len(line)) :
		char = line[i][0]
		for j in range(0, line[i][1]) :
			result +=char
	print(result)

##python have methods 
# "".join(list) : list to string , 
# str.split() : string to list

#'with' open() 'as' fwrite  = like try() catch () finally()

# with open("data.pickle", "wb") as fwrite :	# fwrite = open("data.pickle", "wb")
# 	pickle.dump(res.text, fwrite)

# with open("data.pickle", "rb") as fread : 	# fread = open("data.pickle", "rb")
# 	data = pickle.load(res.text)

