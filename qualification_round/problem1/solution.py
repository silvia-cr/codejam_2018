IMPOSSIBLE = 'IMPOSSIBLE'


def calculate_damage(program):

    strength = 1
    damage = 0

    for action in program:
        if action == 'S':
            damage += strength
        elif action == 'C':
            strength *= 2
        else:
            raise Exception

    return damage


def main():
    t = int(input())

    for i in range(1, t+1):
        test_case = input().split()
        da = int(test_case[0]) # total damage
        pr = test_case[1] # robot program

        p_reverse = pr[::-1]

        num_moves = 0
        equals = False

        damage = calculate_damage(pr)

        while not equals and damage > da:

            aux = p_reverse.replace('SC', 'CS', 1)

            if aux == p_reverse:
                equals = True
            else:
                num_moves += 1

            p_reverse = aux
            damage = calculate_damage(p_reverse[::-1])

        damage = calculate_damage(p_reverse[::-1])
        if damage > da:
            num_moves = IMPOSSIBLE

        print('Case #{0}: {1}'.format(i, num_moves))


if __name__ == '__main__':
    main()
