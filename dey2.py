# ইউজার থেকে একটি সংখ্যা নিয়ে চেক করুন এটি জোড় নাকি বিজোড়
# Hint: % অপারেটর ব্যবহার কর
"""num = int(input("inter number"))
if num % 2 == 0:
	print("জোর")
else:
    print("বিজোর")"""
    
# মার্ক ইনপুট নিয়ে গ্রেড নির্ধারণ করুন:
# 80-100: A+
# 70-79: A
# 60-69: B
# 50-59: C
# 40-49: D
# 0-39: F
"""mark = int(input("inter your mark : "))
if mark >= 101 :
	print("আপনি অতিরিক্ত সংখ্যা লেখেছেন")
elif mark > 80 :
	print("A+")
elif mark > 70:	
    print("A")
elif mark > 60:
	print("B")
elif mark > 50:
    print("C")
elif mark > 40:
	print("D")
else :
    print("F")"""


# দুইটি সংখ্যা ইনপুট নিয়ে বড়টি প্রিন্ট করুন
# যদি সংখ্যা দুইটি সমান হয় তবে মেসেজ দিন
"""num1 = int(input("inter fast number : "))
num2 = int(input("inter secende number : "))
if num1 == num2:
	print("দুটি সমান নাম্বার")
else :
    print("দুটি ভিন্ন নাম্বার")"""
    
# বয়স ইনপুট নিয়ে চেক করুন:
# 18 বা তার বেশি: "আপনি ভোট দিতে পারবেন"
# 18 এর কম: "আপনি ভোট দিতে পারবেন না"
"""age = int(input("inter your age : "))
if age > 101:
	print("আপনি বেশি সংখ্যা লেখেছেন")
elif age > 18:
    print("আপনার ভোট দেওয়ার বয়স হয়েছে")
else:
    print("আপনার এখনো ভোট দেওয়ার বয়স হয় নাই")"""
    
# দুইটি সংখ্যা ও একটি অপারেটর (+, -, *, /) নিয়ে রেজাল্ট দিন
# ভাগ by zero error handle করুন
A = int(input("inter fast number : "))
B = int(input("inter secende number : "))
C = input("+,-,÷,×, এই গুলোর মধ্যে একটি লেখুন : ")
if C == "+":
	print(A+B)
elif C =="-":
    print(A-B)
elif C == "÷" or C == "/":
    print(A/B)
elif C == "×" or C == "*":
	print(A*B)
else:
    print("eror")	