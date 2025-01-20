
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1_low = name1.lower()
name2_low = name2.lower()

t_count = int(name1_low.count("t")) + int(name2_low.count("t"))
r_count = int(name1_low.count("r")) + int(name2_low.count("r"))
u_count = int(name1_low.count("u")) + int(name2_low.count("u"))
e_count = int(name1_low.count("e")) + int(name2_low.count("e"))

first_digit = int(t_count) + int(r_count) + int(u_count) + int(e_count)

first_digit_str = str(first_digit)

l_count = int(name1_low.count("l")) + int(name2_low.count("l"))
o_count = int(name1_low.count("o")) + int(name2_low.count("o"))
v_count = int(name1_low.count("v")) + int(name2_low.count("v"))
e_count = int(name1_low.count("e")) + int(name2_low.count("e"))

second_digit = int(l_count) + int(o_count) + int(v_count) + int(e_count)

second_digit_str = str(second_digit)

number_final = first_digit_str + second_digit_str

number_final_int = int(number_final)

if number_final_int < 10 or number_final_int > 90:
    print(f"Your score is **{number_final}**, you go together like coke and mentos.")
elif 40 < number_final_int < 50:
    print(f"Your score is **{number_final}**, you are alright together.")
else:
    print(f"Your score is **{number_final}**.")
input("Press enter to close program.")



