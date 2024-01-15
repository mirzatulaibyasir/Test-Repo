#Problem 1
def multiplication_or_sum(num1, num2):
    product = num1 * num2
    if product <= 1000:
        return product
    else:
        return num1 + num2

result = multiplication_or_sum(20, 30)
print("The result is", result)
result = multiplication_or_sum(40, 30)
print("The result is", result)


#Problem 2
previous_num = 0

for i in range(1, 11):
    x_sum = previous_num + i
    print("Current Number", i, "Previous Number ", previous_num, "Sum: ", x_sum)

    previous_num = i


#Problem 3
word = input("Enter word")
print("Original String:", word)

size = len(word)

print("Printing only even index chars")
for i in range(0, size - 1, 2):
    print("index[", i, "]", word[i])


#Problem 4
remove_slice = "Constantinople"
print(remove_slice[1:15:2])

def remove_char(word, n):
    print('Original string: ', word)
    x = word[n:]
    return x

print("Removing characters from string")
print(remove_char("Constantinople", 4))
print(remove_char("Constantinople", 2))