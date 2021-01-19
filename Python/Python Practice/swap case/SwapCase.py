def swap_case(s):
    y=''
    for i in s:
        if i==i.upper():
            y+=(i.lower())
        elif i==i.lower():
            y+=(i.upper())
        
    return (y)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)