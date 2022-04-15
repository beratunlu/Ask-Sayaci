
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

new_name_1 = name1.lower()

new_name_2 = name2.lower()


birinci_t =new_name_1.count("t")
birinci_r=new_name_1.count("r")
birinci_u=new_name_1.count("u")
birinci_e=new_name_1.count("e")

birinci_l =new_name_1.count("l")
birinci_o=new_name_1.count("o")
birinci_v=new_name_1.count("v")

ikinci_t =new_name_2.count("t")
ikinci_r=new_name_2.count("r")
ikinci_u=new_name_2.count("u")
ikinci_e=new_name_2.count("e")

ikinci_l =new_name_2.count("l")
ikinci_o=new_name_2.count("o")
ikinci_v=new_name_2.count("v")

true_birlesimi = birinci_t + birinci_r + birinci_u + birinci_e + ikinci_t + ikinci_r + ikinci_u + ikinci_e

love_birlesimi = birinci_l + birinci_o + birinci_v + birinci_e + ikinci_l + ikinci_o + ikinci_v + ikinci_e

genel_birlesim = str(true_birlesimi) + str(love_birlesimi)

if int(genel_birlesim) < 10 or int(genel_birlesim) > 90:
  print(f"Your score is {int(genel_birlesim)}, you go together like coke and mentos.")

elif int(genel_birlesim) >= 40 and int(genel_birlesim) <= 50 :
  print(f"Your score is {int(genel_birlesim)}, you are alright together.")

else:
  print(f"Your score is {int(genel_birlesim)}.")  


