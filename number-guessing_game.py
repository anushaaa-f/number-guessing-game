import random
num = random.randint(1, 100)
for i in range(6):
    guess = int(input("Enter Your Number:"))
    if guess == num:
        print("Yayy! You got it right")
        break
    elif guess>num:
        print("Aww! Try to guess lower number")
    elif guess<num:
        print("Aww! Try to guess higher number")
else:
    print("No more chances left\nGAME OVER!! The correct number was", num)