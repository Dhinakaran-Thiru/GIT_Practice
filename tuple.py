a=("dhinakaran",)
print(type(a))
b="dhinkaran"
print(type(b))
c=("dhinakaran",)
print(type(c))

#convert list into tuple
A=("dhinakaran","deepa","deepika","nadupatti","kamalakannan")
B=list(A)
B[1]="naveen kumar"
A=tuple(B)
print(A)
"""for i in range(0,99):
    print("99x",i,"=" ,i*99)"""
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)
tuple1=["dhinakaran","deepika","deepa"]
tuple2=list(tuple1)
tuple2[0]="deena"
tuple1=tuple(tuple2)
print(tuple1)



thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

