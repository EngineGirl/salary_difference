def rev(time, salary, per):
    total = salary
    day = time * 365
    for i in range(day):
        if i != 0 and i % 31 == 0:
            total += salary
        total = total + total * per/100/365
    return total

print(rev(10, 1000, 4))
