x, y, z = int(input("Input lengths of the triangle sides: x: ")), int(input("y: ")), int(input("z: "))
if x == z and x == y and y == z:
    print("equilateral")
elif x != z and x != y and y != z:
    print("scalene")
else:
    print("isosceles")
#done