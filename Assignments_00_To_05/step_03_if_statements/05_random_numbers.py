import random

def main():
  number = []
  for i in range(10):
    number.append(random.randint(1,100)) 
  print(number)

if __name__=="__main__":
 main()