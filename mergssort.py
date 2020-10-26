def mergesort(list) :
  if len(list)<=1 :
    return(list)
  else :
    halflen = int(len(list)/2)
    sorted_right_list = mergesort(list[halflen:len(list)])
    sorted_left_list =  mergesort(list[0:halflen])
    right_ptr = 0
    left_ptr = 0
    output_list = []
    for x in range(len(list)) :
      if sorted_right_list[right_ptr] < sorted_left_list[left_ptr] : 
        output_list.append(sorted_right_list[right_ptr])
        right_ptr = right_ptr + 1
        if right_ptr == len(sorted_right_list): 
          sorted_right_list.append(99999999)
      else :
        output_list.append(sorted_left_list[left_ptr])
        left_ptr = left_ptr + 1
        if left_ptr == len(sorted_left_list) : 
          sorted_left_list.append(99999999)
    return(output_list)

print(mergesort([4,5,8,2,3]))


