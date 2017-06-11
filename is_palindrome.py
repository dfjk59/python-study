#回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()滤掉非回数：
def is_palindrome(n):
    return n > 10 and str(n) == str(n)[::-1]

output = filter(is_palindrome, range(1, 1000))
print(list(output))
