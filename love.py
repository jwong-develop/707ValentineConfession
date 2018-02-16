import time

for i in range(15):
  print("\n\n")
print("Dear 707, Defender of Justice,\n")

print("The cheerful cat robot you made can brighten the darkest of days. I know you have a lot of dark days, so I think you deserve something to cheer you up too! I'm not very good at building robots, but I hope it can brighten a day or two for you, too <3\n")

print("Solve the 'hacker' riddles for a fun surprise!\n")

answer = ''

print("First riddle! Decode the following:")
hint1 = False
while not (answer == '707'):
  if hint1:
    print("\nNope, try again!\nHint: binary for a very special number")
  answer = raw_input("0010 1100 0011\n")
  hint1 = True
print("\nThat's right, it's you! The sweetest genius on the entire planet - and space.\n")

print("You're amazing! Ready for the next one?")
hint2 = False
while not (answer.lower() == 'xff0000' or answer.lower() == 'ff0000' or answer.lower() == '#ff0000'):
  if hint2:
    print("\nTry again!\nHint: beautiful red, just like your baby car")
  answer = raw_input("What's the hex color of your heart?\n")
  hint2 = True
print("\nNice! On to riddle #3! Woot woot! Halfway there!!\n")

print("Decrypt this coded message:")
hint3 = [False, False]
while not (answer.lower() == 'saeran'):
  if hint3[0] and not hint3[1]:
    print("\nTry again!\nHint 1 of 2: letter cypher + index of character!")
    hint3[1] = True
  elif hint3[0] and hint3[1]:
    print("\nSorry, still no! Keep trying though! I know you'll get it!\nHint 2 of 2: important twin brother")
  answer = raw_input("sbgues\n")
  hint3[0] = True
print("\nYou really are a genius! Last riddle!\n")

hint4 = False
while not(answer.lower() == 'i love you'):
  if hint4:
    print("\nSorry, try again!\nHint: it's how I feel about you!")
  answer = raw_input("Translate 'Saranghae' from Korean to English!\n")
  hint4 = True

print("\nYeah! You did it. And I meant it. Saranghae. I love you.")
print("Do you want to know what your prize is?")
print("It's a trip to space! I hope you love it as much as I love you <3 \n\n")

print("             *                        *     *             *")
print("      *              *                         *        *  ")
print("          *                        *                *      ")
print("                          *                 *              ")
print("       *         *             *                           ")
print("  *                  *                  *      *        *  ")
print("               _________________                           ")
print("          *    [               ]                           ")
print("               [  space        ]           *         *     ")
print("   *           [      station  ]    *           *          ")
print("               [               ]                           ")
print("               -----------------            *              ")
print("          *                         *                      ")
print(" *                  *          *                         * ")
print("            *                                              ")
print("                             *                 *           ")
print("    *                                                      ")
print("                   *              *                *       ")

print("\n")
print("I'll be waiting for you at the space station.")

print("\n\n")
time.sleep(45000)
