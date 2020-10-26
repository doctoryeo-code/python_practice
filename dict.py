thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(x , "==>", thisdict[x])


thisdict["year"] = 1971
print(thisdict["year"])


if "model" in thisdict:
  print("Yes, model is a key in thisdict")
if "smodel" in thisdict:
  print("Yes, smodel is a key in thisdict")

