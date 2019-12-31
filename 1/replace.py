#http://www.pythonchallenge.com/pc/def/map.html
A= "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

print(A);

print

B="";


for i in range(0,len(A)):
    if ord(A[i]) >= 97 :    #this is alphabet
        tran = ord(A[i])+2  #ord() is chr to ascii
    
        if tran >122:       #ascii(122) ='z'
            tran-=26        #122-26 = 97 , ascii(97) = a
    else :
        tran = ord(A[i])
    
    B += chr(tran)

print(B);

