number = ("random number")
import random
answer = random.randint(1, 10)
count = 0
while True:
    number = int(input("ใส่ตัวเลขที่คุณทาย1-10"))
    count +=1

    if number>answer:
        print("มากไปทายใหม่")
    elif number<answer:
        print("น้อยไปทายใหม่")
    else:
        print("ถูกต้อง")
        print("คุณท้ายทั้งหมด", count, ("ครั้ง"))
        break