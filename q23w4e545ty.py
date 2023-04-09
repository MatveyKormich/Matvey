def raise_to_the_degrees(number, max_degree):
    for i in range(max_degree + 1):
        yield number ** i

res = raise_to_the_degrees(2, 10)
print(res)

for _ in res:
    print()