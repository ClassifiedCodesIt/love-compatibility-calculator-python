print("Welcome to the Classified Love Compatibility Calculator!")
name1 = input("What is your name?\n")
name2 = input("What is their name?\n")
combined_names = name1 + name2
lower_names = combined_names.lower()
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
score1 = t + r + u + e
l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
score2 = l + o + v + e
print("The Classified Love Compatibility Calculator is calculating your score...")
score_total = int(str(score1) + str(score2))
if (score_total < 10) or (score_total > 90):
  print(f"Your score is {score_total}, you are perfect together!")
elif (score_total >= 40) and (score_total <= 50):
  print(f"Your score is {score_total}, you are alright together.")
else:
  print(f"Your score is {score_total}.")