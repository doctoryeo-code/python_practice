def annagram ( word1, word2 ) :
  if len(word1) != len(word2) :
    print(word1, word2, "are NOT annagram")
    return 0
  else :
    listword1 = list(word1)
    listword2 = list(word2)
    listword1.sort()
    listword2.sort()
    if listword1 == listword2 :
      print(word1, word2, "are annagram")
      return 1
    else :
      print(word1, word2, "are NOT annagram")
      return 0





annagram("they", "yeht")
annagram("hhey", "yeht")
annagram("hhey", "yeh")
