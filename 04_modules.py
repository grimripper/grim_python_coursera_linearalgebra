i = 0
while True:
    print ('hello', i)
    i = i+1
    if i >= 5: break

f = open('matrix\stories_big.txt')
stories = list(f)
print(len(stories))
