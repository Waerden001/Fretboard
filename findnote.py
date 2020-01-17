def find_all(spot):
    ans = []
    for string in range(1,7):
        modification = 0
        if string>spot[1] and 5<=string:
            modification = -1
        if spot[1]>string and 5<=spot[1]:
            modification = 1
        for fret in range(0,25):
            if (5*(string-spot[1])+modification+(fret-spot[0]))%12==0:
                ans.append([fret, string])
    return ans

def coordinate(ans):
    for ele in ans:
        print(str(ele[1])+'/'+str(ele[0]),end=",")
