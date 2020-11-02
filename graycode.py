def graycode (x, bw) :
  y = bin(x)

  #Get rid of preceding "0b" prefix
  y = y[2:]

  #Sign Extend
  while len(y)!=bw :
    y = "0"+y

  #Reverse the order of bits of y
  z = y[::-1]
  s = ""
  for index in range(0,len(z)-1) :
    zi=int(z[index])
    zii=int(z[index+1])
    if zii==1 : 
      a = str(1 - zi)
    else :
      a = str(zi)
    s = s+a 
    print(s)
  s = s+z[-1]
  return s[::-1]



graycode5 = lambda(x) : graycode(x,5)

x = range(0,32)
#graycode5(2)
y = map(graycode5, x)
print("GrayCode of " , x , " = " , y)

