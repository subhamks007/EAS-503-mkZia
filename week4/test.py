def simulate_two_dice(no_simulation):
    import random
    theoretical_probabilities = [
        0,
        0,
        1 / 36,
        2 / 36,
        3 / 36,
        4 / 36,
        5 / 36,
        6 / 36,
        5 / 36,
        4 / 36,
        3 / 36,
        2 / 36,
        1 / 36,
    ]

    two_dice = {}

    for no in range(no_simulation):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        total = dice1 + dice2
        if total not in two_dice:
            two_dice[total] = 0

        two_dice[total] += 1

    simulated_probability = [0, 0]

    for number in range(2, 13):
        simulated_probability.append(two_dice[number] / no_simulation)

    column1 = 'Total'
    column2 = 'Simulated Percent'
    column3 = 'Expected Percent'

    print(
        column1.ljust(6),
        column2.rjust(20),
        column3.rjust(20),
        '\n'
    )
    for number in range(2, 13):
        sp = round(simulated_probability[number] * 100, 2)
        tp = round(theoretical_probabilities[number] * 100, 2)
        print(
            str(number).ljust(6),
            str(sp).rjust(20),
            str(tp).rjust(20),
        )


simulate_two_dice(1000000)
