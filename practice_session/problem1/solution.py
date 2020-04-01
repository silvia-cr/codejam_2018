TOO_SMALL = "TOO_SMALL"
TOO_BIG = "TOO_BIG"
WRONG_ANSWER = "WRONG_ANSWER"
CORRECT = "CORRECT"

def main():
    t = int(input())

    for i in range(1, t+1):
        inp = input().split()
        low_limit = int(inp[0])+1
        high_limit = int(inp[1])

        nn = int(input())

        guess = False

        while not guess:
            qq = (low_limit + high_limit)//2
            print(qq, flush=True)
            response = input()

            if response == CORRECT:
                guess = True
            elif response == TOO_BIG:
                high_limit = qq
            elif response == TOO_SMALL:
                low_limit = qq
            else: #wrong answer
                break


if __name__ == '__main__':
    main()
