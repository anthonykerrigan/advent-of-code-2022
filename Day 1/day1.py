elflist = open("Calories.txt","r")

#Challenge 1
#print(max(sum(int(i) for i in x.split ()) for x in elflist.read().split('\n\n')))

#challenge 2
def top3(f):
    a = [sum(int(i) for i in x.split()) for x in f.read().split("\n\n")]
    ans = max(a)
    a.remove(max(a))
    ans += max(a)
    a.remove(max(a))
    ans += max(a)
    return ans

print(top3(elflist))

elflist.close()