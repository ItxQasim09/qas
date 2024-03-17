print("Welcome to KBC\n".center(43))
t= "You will be asked questions \nand you would win cash prize\nfor every correct answer\n\n"
b_i= "\033[1m\033[3m" + t + "\033[0m"
print(b_i)
print(input("Press Enter to continue...."))
questions= ["A. What is the capital of Pakistan?",
            "B. Which city is known as City of Lights?",
            "C. Who is founder of Pakistan?"
            "D. You wanna learn python?"
            "E. Which language used to design FB?" ]
def mcq(choices):
  for i, answer in enumerate(choices,start= 1 ):
    print(f"{i} . {answer}")
levels= [1000, 5000, 10000, 50000, 100000, 250000, 500000]
money = 0


def inpu(a):
    ans = int(input("Enter your answer (1-4) or type 0 to exit: "))

    if ans == 0:
        print("Exiting...")
    elif ans == a:
        print(f"Correct Answer! You won Rs. {levels[0]}")
        proceed = input("Enter 'yes' to proceed to the next level, or type 'exit' to quit: ")
        if proceed == 'yes':
            for i in range(1, len(levels)):
                print(f"Congratulations! You won Rs. {levels[i]}")
        else:
            print("Exiting...")
    else:
        print("Wrong Answer")



c1= ["Islamabad", "Karachi", "Lahore", "Quetta"]
c2= ["Islamabad", "Karachi", "Lahore", "Quetta"]
c3= ["Allama Iqbal", "Molana Altaf", "M. Ali Jinnah", "Sir Syed"]
c4= ["Yes", "No", "Maybe in future", "Not sure"]
c5= ["Python", "C++", "Java", "php"]
print(f"Your 1st Question for Rs. {levels[0]} is:\n")
print (questions[0])
mcq(c1)
inpu(1)

print(f"Your 2nd Question for Rs. {levels[1]} is:\n")
print(questions[1])
mcq(c2)
inpu(2)




def inpu(a):
  while True:
    ans= int(input("Enter your answer (1-4) or type 0 to exit: \n"))
    if ans == 0:
      print("Exiting...")
      break
    elif ans == a:
      print(f"Correct Answer! You won {levels[len(levels)-1]}")
      for i, prize in enumerate(levels, start =1):
        print(f"Prize is Rs.{prize}")
    else:
      print("Wrong Answer")
      break
