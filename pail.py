def pail (large, small, target) :
  #large : size of large pail
  #small : size of small pail
  #target : Need to measure this size

  small_pail_content = 0
  large_pail_content = 0;
  while large_pail_content != target :
    #Fill large pail
    large_pail_content = large;
    
    #Pour contents of large pail into small pail until small pail is full
    large_pail_content = large_pail_content - small + small_pail_content
    small_pail_content = small
    print(large_pail_content)
 
    #Check contents of large pail
    if large_pail_content == target :
      exit()
 
    #Pour away contents of small pail
    small_pail_content = 0
 
    #Pour contents of large pail into small pai.
    small_pail_content = large_pail_content
    large_pail_content = 0

    print("iter")


a=9
b=7
c=8
pail(a,b,c)
