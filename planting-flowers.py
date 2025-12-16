def canPlaceFlowers(flowerbed, n):
    count = 0
    length = len(flowerbed)

    for i in range(length):
        # TODO: What conditions should we check here?
        if (
            flowerbed[i] == 0
            and (i == 0 or flowerbed[i - 1] == 0)
            and (i == length - 1 or flowerbed[i + 1] == 0)
        ):
            # Plant a flower here
            flowerbed[i] = 1
            count += 1
            if count >= n:
                return True
    return count >= n

def check_arguments(list, count):
    initial = list.copy()
    print("CanPlaceFlowers:", initial, " with count=", count, " result=", canPlaceFlowers(list, count), " with: ", list)

check_arguments([0,0,0,0], 3)
check_arguments([0], 2)
check_arguments([0], 3)
check_arguments([0, 0], 2)
check_arguments([0, 0], 3)

check_arguments([0,0,0,1], 3)
check_arguments([1,0,0,0,0,1], 2)
