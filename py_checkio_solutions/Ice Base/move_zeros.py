#!/usr/local/bin/checkio --domain=py run move-zeros


def move_zeros(items):
    result = [i for i in items if i != 0]
    result += [0] * (len(items) - len(result))
    return result


print("Example:")
print(move_zeros([0, 1, 0, 3, 12]))

assert move_zeros([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0]
assert move_zeros([0]) == [0]

print("The mission is done! Click 'Check Solution' to earn rewards!")
