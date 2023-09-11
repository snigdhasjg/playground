# https://leetcode.com/problems/minimum-penalty-for-a-shop/


def penalty_at_time(customer_visits: list[str], time: int):
    penalty = 0
    penalty_states = []
    for idx, status in enumerate(customer_visits):
        if idx < time:
            shop_open_no_customer_penalty = 1 if status == 'N' else 0
            penalty_states.append(f'{shop_open_no_customer_penalty}')
            penalty += shop_open_no_customer_penalty
        else:
            customer_come_shop_closed_penalty = 1 if status == 'Y' else 0
            penalty_states.append(f'{customer_come_shop_closed_penalty}')
            penalty += customer_come_shop_closed_penalty
    print(f'{" + ".join(penalty_states)} : {penalty} at index({time})')
    return penalty


def find_minimal_penalty(customer_arrival_indicator: str):
    customer_visits = list(customer_arrival_indicator)
    return min(
        [(idx, penalty_at_time(customer_visits, idx)) for idx in range(len(customer_visits) + 1)],
        key=lambda x: x[1]
    )


def initial_count(customer_visits: list[str]):
    count_y = 0
    count_n = 0
    for status in customer_visits:
        if status == 'Y':
            count_y += 1
        else:
            count_n += 1

    return {'Y': count_y, 'N': count_n}


def minimal_penalty(customer_arrival_indicator: str):
    customer_visits = list(customer_arrival_indicator)
    right_side_count = initial_count(customer_visits)
    left_side_count = {'Y': 0, 'N': 0}

    def find_difference():
        return left_side_count['N'] + right_side_count['Y']

    minimum_penalty = (0, find_difference())

    def print_counts():
        print(f'left: {left_side_count} right: {right_side_count} with minimum penalty: {minimum_penalty}')

    print_counts()

    for idx, status in enumerate(customer_visits):
        left_side_count[status] += 1
        right_side_count[status] -= 1

        penalty = find_difference()
        if minimum_penalty[1] > penalty:
            minimum_penalty = (idx + 1, penalty)

        print_counts()

    return minimum_penalty


if __name__ == '__main__':
    print(minimal_penalty('YYNYYNNY'))
    print(find_minimal_penalty('YYNYYNNY'))
