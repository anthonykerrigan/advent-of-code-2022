tourney = open("jankenpon.txt", "r")

# Assign numerical values to Rock, Paper and Scissors.


# Define a "win"
def win(f): 
    ans = 0
    
# Scan the input 
    for line in f: 
        a, b = line.split()
        a = "ABC".index(a)
        b = "XYZ".index(b)

        ans += b + 1

        match(b-a) % 3:
            case 1: 
                ans += 6 
            case 0:
                ans += 3

    return ans

def p2(f):
    ans = 0

    for line in f:
        a, b = line.split()
        a = "ABC".index(a)

        match b:
            case "X":
                ans += (a - 1) % 3 + 1
            case "Y":
                ans += 3
                ans += a + 1
            case "Z":
                ans += 6
                ans += (a + 1) % 3 + 1

    return ans

#print(win(tourney))

print(p2(tourney))

# Determine numerical total of your score

tourney.close()
    #rock = 1
    #paper = 2
    #scissors = 3
    #win = 6
    #draw = 3
    #loss = 0