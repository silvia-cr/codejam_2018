def main():
    t = int(input())

    for i in range(1, t + 1):
        nu = int(input())
        va = list(map(int, input().split()))

        end = False

        while not end:
            end = True
            for idx in range(0, nu - 2):
                if va[idx] > va[idx + 2]:
                    aux = va[idx]
                    va[idx] = va[idx + 2]
                    va[idx + 2] = aux
                    end = False

        end = False
        idx = 0
        while not end and idx < nu - 1:
            if va[idx] > va[idx+1]:
                end = True
            else:
                idx += 1

        if not end:
            result = 'OK'
        else:
            result = str(idx)

        print('Case #{0}: {1}'.format(i, result))


if __name__ == '__main__':
    main()
