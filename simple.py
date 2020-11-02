#/stQuestions from 
#/https://pynative.com/python-basic-exercise-for-beginners/

def q1(a,b) :
  if (a*b>1000) :
    return (a*b)
  else :
    return -1

def q2(start) :
  y = 0
  for x in range (start , start+10) :
    print(" sum of " , x , " and " , y, " = " , x+y)
    y = x


def q3(input_string) :
  print(input_string)
  index = 0
  for x in input_string :
    if index%2 == 0 :
      print("char = " , x)
    index = index+1

  
def q4(input_string, n) :
  return input_string[n:]

def q4_2(input_string, n) :
  return input_string[:n]

def q5(num_list) :
  if num_list[0] == num_list[-1] :
    return True
  else :
    return False


def q7(input_string) :
  count = 0
  for x in range (0, len(input_string)-3) :
    if input_string[x:x+4] == "Emma" : 
      count = count+1
  return count

def q8() :
  for x in range (1,6) :
    output_string = str(x)
    for y in range (1, x) :
      output_string = output_string + " " + str(x) 
    print output_string


print("3 * 2 = " , q1(3,2))
print("300 * 200 = ", q1(300,200))
q2(200)
q2(1)
q3("i want to tell you")

print(q4("superboy", 5))
print(q4_2("superboy", 5))

print(q5([5, 4, 3, 2, 1, 0]))
print(q5([5,4,3,2,1,5]))


print(q7("Emma is good developer. Emma is Emma"))

q8()
