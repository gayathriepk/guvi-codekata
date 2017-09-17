def main():
    string = str(input("Enter the string : "))
    integer = str_to_int(string)
    print("the integer are:%d",integer)

def str_to_int(x):
    count = res = 0
    for a in reversed(ex):
        res += (ord(a) - 48) * 10 ** count
        count += 1
    return res

if __name__ == '__main__':
    main()
   