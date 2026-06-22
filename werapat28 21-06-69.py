print("โปรแกรมคำนวณคะแนนรวม\n")
physical = int(input("คะแนนวิชาพละ"))
health = int(input("คะแนนวิชาสุขศึกษา"))
computer = int(input("คะแนนวิชาคอมพิวเตอร์"))

total_point =  physical + health + computer
average = total_point/3
if average < 60 : 
    print("\nแสดงคะแนนรวม = ",total_point,"คะแนน")
    print("แสดงคะแนนเฉลี่ย 3 วิชา = " ,average)
elif average < 80:
    print("แสดงคะแนนรวม = ",total_point,"คะแนน")
    print("ผ่าน")
else:
    print("แสดงคะแนนรวม = ",total_point,"คะแนน")
    print ("ดีเยี่ยม")
print("\nโดย วีรภัทร หมื่นแทน เลขที่28 ม.4/4")