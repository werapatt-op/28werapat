print("โปรแกรมคำนวณคะแนนรวม\n")
physical = int(input("คะแนนวิชาพละ"))
health = int(input("คะแนนวิชาสุขศึกษา"))
computer = int(input("คะแนนวิชาคอมพิวเตอร์"))

total_point =  physical + health + computer
average = total_point/3
print("\nแสดงคะแนนรวม = ",total_point,"คะแนน")
print("แสดงคะแนนเฉลี่ย 3 วิชา = " ,average)
if average < 60 : 
    print("\nควรปรับปรุง")
elif average < 80:
    print("แสดงคะแนนรวม = ",average)
    print
    print("ผ่าน")
else:
    print("แสดงคะแนนรวม = ",average)
    print ("ดีเยี่ยม")
print("\nโดย วีรภัทร หมื่นแทน เลขที่_28 ม.4/4")