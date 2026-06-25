print("ตรวจจับความเร็ว")
Speed = int(input("km/h"))
total = (Speed)

if   total <80:
     print("ปลอดภัย")
elif total <100:
     print("เตือน")
elif total <120:
     print("เสี่ยงถูกปรับ")
else:
     print("ผิดกฎหมายปรับทันที")
print("สถานะความปลอดภัย")