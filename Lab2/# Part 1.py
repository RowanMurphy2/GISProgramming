# Part 1
part1 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]

results1 = 1
for i in part1:
    results1 = results1 * i

print('the results of the frist part is:', results1)

# Part 2
part2 = [-1, 23, 483, 8573, -13847, -381569, 1652337, 718522177]

results2 = 0
for i in part2:
    results2 = results2 + 1

print('the results of the second part is:', results2)

# Part 3
part3 = [146, 875, 911, 83, 81, 439, 44, 5, 46, 76, 61, 68, 1, 14, 38, 26, 21]

results3 = 0
for i in part3:
    if i % 2 == 0:
        results3 = results3 + i

print('the results of the third part is:', results3)