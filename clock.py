def sum(t1 , t2):
    result = {}
    result["h"] = t1["h"] + t2["h"]
    result["m"] = t1["m"] + t2["m"]
    result["s"] = t1["s"] + t2["s"]

    if result["s"] >= 60:
        result["s"] -= 60
        result["m"] +=1

    if result["m"] >= 60:
        result["m"] -= 60
        result["h"] +=1

    return result

def show(result):
    print(f"{result['h']} : {result['m']} : {result['s']}")

def tafrigh(t1 , t2):
    result = {}
    result["h"] = t1["h"] - t2["h"]
    result["m"] = t1["m"] - t2["m"]
    result["s"] = t1["s"] - t2["s"]

    if result["s"] < 0:
        result["m"] -= 1
        result["s"] += 60

    if result["m"] < 0:
        result["h"] -= 1
        result["m"] += 60

    return result      

h1 = int(input("Enter hour1: "))
m1 = int(input("Enter minute1 :"))
s1 = int(input("Enter second1: "))
h2 = int(input("Enter hour2: "))
m2 = int(input("Enter minute2: "))
s2 = int(input("Enter second2: "))

time1 = {"h" :h1, "m" :m1, "s" :s1}
time2 = {"h" :h1 , "m" :m2 , "s" :s2}

result_s = sum(time1 , time2)
print(result_s)

show(result_s)

result_t = tafrigh(time1 , time2)
print(result_t)

show(result_t)