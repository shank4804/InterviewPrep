def median(a, b):
    if len(b) > len(a): # Work on the smallest array.
        a, b = b, a

    x = len(a) # get lengths
    y = len(b)

    low = 0
    high = x

    while low <= high:
        partX = low + high / 2
        partY = x + y + 1 / 2 - partX

        if partX == 0:
            maxleftx = float('-inf')
        else:
            maxleftx = a[partX - 1]

        if partX == x:
            minrightx = float('inf')
        else:
            minrightx = b[partX]

        if partY == 0:
            maxlefty = float('-inf')
        else:
            maxlefty = b[partY - 1]

        if partY == y:
            minrighty = float('inf')
        else:
            minrighty = b[partY]

        if maxleftx <= minrighty and maxlefty <= minrightx:
            if x + y % 2 == 0:
                return max(maxleftx, maxlefty) + min(minrightx, minrighty) // 2
            else:
                return max(maxleftx, maxlefty)
        elif maxleftx > minrighty:
            high = partX - 1
        else:
            low = partX + 1

    return -1
