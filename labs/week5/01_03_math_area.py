# write a function that takes the length and width of a rectangle and returns the area
def area(l,b):
    a = l*b
    return a


def areacube(l,b):
    if l == b:
        face_area = area(l,b)
        area = 6 * face_area
        print("Both are not equal there for the area is : ")
        print(area)
    else:
        print("Both are not equal")
        return None

def areasp(r):
    a=4*(22/7)*(r**2)
    print(a)


areacube(8,8)
# areasp(5)


# write another function that finds the area of a cube
# def areacube(s):
#     a=6*s
#     print(a)
# bonus challenge: use your first function inside this function!

# area(8,9)
# areacube(4)

# hint: you can get `pi` by importing math (google it!)


# write a function that finds the area of a sphere