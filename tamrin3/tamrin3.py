counter = 0

def No_Zero_In_Number(number):
    x = str(number)
    return "0" not in x  


def only_have_2_number(number):
    number_str = str(number)
    part1 = int(number_str[0])
    part2 = int(number_str[1])
    part3 = int(number_str[2])
    p = set()
    p.add(part1)
    p.add(part2)
    p.add(part3)
    return len(p) == 2 




for i in range(100, 1000):
    if No_Zero_In_Number(i) and only_have_2_number(i):
        counter += 1

print(counter)