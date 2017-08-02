def bubble_sort(l):
    lc = l[::]

    def swap(i, j):
        aux = lc[i]
        lc[i] = lc[j]
        lc[j] = aux

    for i in range(len(lc)-1):
        for j in range(len(lc)-(i+1)):
            print("({} < {})".format(lc[j+1], lc[j]))
            if lc[j+1] < lc[j]:
                print("({}: {} <- {}: {})".format(j, lc[j], j+1, lc[j+1]))
                swap(j, j+1)

        print(lc)
        print("--")
    return lc

l = [10,9,8,7,6,5,4,3,2,1]
print(l)
new = bubble_sort(l)

print("from {} to {}".format(l, new))
