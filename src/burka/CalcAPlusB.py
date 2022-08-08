import sys

print(f"Arguments count: {len(sys.argv)}")
print(sys.argv[0])
print("param1 is " + sys.argv[1])
print("param2 is " + sys.argv[2])
print("param3 is " + sys.argv[3])

print("ну а теперь выведем сумму первых двух параметров:")

print(int(sys.argv[1]) + int(sys.argv[2]))


