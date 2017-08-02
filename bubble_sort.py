def bubble_sort(l):
    lc = l[::]

    def swap(i, j):
        aux = lc[i]
        lc[i] = lc[j]
        lc[j] = aux

    for i in range(len(lc)-1):
        swaps = 0
        for j in range(len(lc)-(i+1)):
            if lc[j+1] < lc[j]:
                print("({}: {} <- {}: {})".format(j, lc[j], j+1, lc[j+1]))
                swap(j, j+1)
                swaps = swaps + 1

        print("resulting list: {} with {} swaps".format(lc, swaps))
        print("--")
    return lc

l = [10,9,8,7,6,5,4,3,2,1]
new = bubble_sort(l)

print("from {} to {}".format(l, new))
