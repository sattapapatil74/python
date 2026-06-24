def a_m(m):
    if len(m) == 0:
        return 0
    return sum(m)/len(m)

s_m=[23,3,45,12,34]
a=a_m(s_m)
print("average marks:",a)