import random

def read_print():
  print("Keep it logically awesome.")
  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  last = len(quotes)-1
  rnd = random.randint(0,last)
  print(quotes[rnd].strip())
  while 1:
    rnd2 = random.randint(0,last)
    if rnd2 != rnd:
      break
  print(quotes[rnd2].strip())

def write_print():
  f = open("quotes.txt","a+")
  f.writelines("写入成功")
  f.close()

if __name__== "__main__":
  write_print()
  read_print()
