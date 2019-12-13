print("\n---------- PART ONE ----------")


def check_if_inc(number: int) -> bool:
    number_str = str(number)
    current = 0
    for index in range(0, len(number_str)):
        value = int(number_str[index])
        if value < current:
            return False
        if value > current:
            current = value
    return True


def check_if_two_times_in_inc(number: int) -> bool:
    number_str = str(number)
    current = int(number_str[0])
    for index in range(1, len(number_str)):
        value = int(number_str[index])
        if current == value:
            return True
        current = value
    return False


def check_if_two_times_in_inc_no_group(number: int) -> bool:
    number_str = str(number)
    current = int(number_str[0])
    occ = 1
    for index in range(1, len(number_str)):
        value = int(number_str[index])
        if current == value:
            occ += 1
        else:
            if occ == 2:
                return True
            occ = 1
        current = value

    # check last index
    if occ == 2:
        return True
    return False


# 111111 meets these criteria (double 11, never decreases).
# 223450 does not meet these criteria (decreasing pair of digits 50).
# 123789 does not meet these criteria (no double).
print("111111 should be True:", check_if_inc(111111) and check_if_two_times_in_inc(111111))
print("123789 should be False:", check_if_inc(123789) and check_if_two_times_in_inc(123789))
print("223450 should be False:", check_if_inc(223450) and check_if_two_times_in_inc(223450))

start = 125730  # 0
end = 579381  # pow(10, 6) - 1
numbers = []
for n in range(start, end + 1):
    if check_if_inc(n) and check_if_two_times_in_inc(n):
        numbers.append(n)
print("from:", start, "to:", end, "there is:", len(numbers), "numbers correct")

print("\n---------- PART TWO ----------")

# 112233 meets these criteria because the digits never decrease and all repeated digits are exactly two digits long.
# 123444 no longer meets the criteria (the repeated 44 is part of a larger group of 444).
# 111122 meets the criteria (even though 1 is repeated more than twice, it still contains a double 22).
print("112233 should be True:", check_if_inc(112233) and check_if_two_times_in_inc_no_group(112233))
print("123444 should be False:", check_if_inc(123444) and check_if_two_times_in_inc_no_group(123444))
print("111122 should be True:", check_if_inc(111122) and check_if_two_times_in_inc_no_group(111122))

numbers = [number for number in numbers if check_if_two_times_in_inc_no_group(number)]

print("from:", start, "to:", end, "there is:", len(numbers), "numbers correct")
