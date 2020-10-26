"""
Convert a hex number to decimal
"""
def foofunc(ain):
  ad = 0
  for x in ain:
    ad = ad*16
    if x <= 9 :
      ad = ad + x
    else:
      ad = ad + ord(x) - ord('a') + 10
    """
    elif x == "a" :
      ad = ad + 10
    elif x == "b" :
      ad = ad + 11
    elif x == "c" : 
      ad = ad + 12
    elif x == "d" :
      ad = ad + 13
    elif x == "e" :
      ad = ad + 14
    else:
      ad = ad + 15
    """
  return ad

print(foofunc("f0ff"))
