print("Eutimio machuca parra A01630244")
def tringles(size):
    size = int(input("what size of triangle do you wamt? "))
    for r in range(1, size+1):
        for c in range(1, r+1):
            print('T', end = "")
        print ()
    for r in range(size - 1, 0, -1):
        for c in range(1, r, 1):
            print('T', end = "")
        print()
ans=1
while(ans!=0):
    tri=tringles('size')
    print(tri)
    ans=int(input(print(" do you wanna try again? 0-NO 1- YES")))