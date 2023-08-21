print("Salam! man mitonam javab jam , zarb , tafrigh va taghsim do kasr ro behet bedam.")

# (2 / 3) + (4 / 5) = (2*5) + (4*3) / (3*5)
def sum(a1,a2):
    result = {}
    result["s"] = (a1["s"] * a2["m"]) + (a2["s"] * a1["m"])
    result["m"] = a1["m"] * a2["m"]
    return result

# (2 / 3) * (4 / 5) = (8 / 15)
def multipy(a1,a2):
    result = {}
    result["s"] = a1["s"] * a2["s"]
    result["m"] = a1["m"] * a2["m"]
    return result

# (2 / 3) - (4 / 5) = (2*5) - (4*3) / (3*5)
def tafrigh(a1,a2):
    result = {}
    result["s"] = (a1["s"] * a2["m"]) - (a2["s"] * a1["m"])
    result["m"] = a1["m"] * a2["m"]
    return result

# (2 / 3) / (4 / 5) = (2*5) / (4*3)
def taghsim(a1,a2):
    result = {}
    result["s"] = a1["s"] * a2["m"]
    result["m"] = a1["m"] * a2["s"]
    return result

def show(result):
    print(f"{result['s']} / {result['m']}")

s1 = float(input("Soorat kasr aval: "))
m1 = float(input("Makhraj kasr aval: "))
s2 = float(input("Soorat kasr dovom: "))
m2 = float(input("Makhraj kasr dovom: "))

f1 = {"s" : s1 , "m" : m1}
f2 = {"s" : s2 , "m" : m2}

result_s = sum(f1,f2)
show(result_s)

result_m = multipy(f1,f2)
show(result_m)

result_t1 = tafrigh(f1,f2)
show(result_t1)

result_t2 = taghsim(f1,f2)
show(result_t2)