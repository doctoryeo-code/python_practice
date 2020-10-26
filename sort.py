def sort(list) :
  if len(list)==1 :
    return(list)
  elif len(list)==2 :
    if list[0] > list[1] :
      return([list[1], list[0]])
    else :
      return(list)
  else :
    sorted_right_list = sort(list[1:])
    output_list = sorted_right_list
    print(sorted_right_list)
    i = 0
    for x in sorted_right_list :
      if list[0] > x :
        i = i + 1
    output_list.insert(i, list[0])
    return(output_list)

print(sort([4,5,3,1,2]))


