filenames = ["1.Data.txt","2.Law.txt","3.Present.txt"]

for filename in filenames:
  filename = filename.replace('.','-',1) #(what need to replace,with what, how many form 1st occurance)
  print(filename)