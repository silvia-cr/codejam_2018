def main():
    t = int(input())

    for i in range(1, t + 1):
        nu = int(input())
        va = list(map(int, input().split()))
        original = va

        end = False

        while not end:
            end = True
            for idx in range(0, nu - 2):
                if va[idx] > va[idx + 2]:
                    aux = va[idx]
                    va[idx] = va[idx + 2]
                    va[idx + 2] = aux
                    end = False

        if sorted(original) == va:
            result = 'OK'
        else:
            result = 0
            end = False
            while result < len(va) and not end:
                if va[result] > va[result+1]:
                    end = True
                else:
                    result += 1

        print('Case #{0}: {1}'.format(i, result))


if __name__ == '__main__':
    main()
