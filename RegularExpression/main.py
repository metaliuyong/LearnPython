import re

if __name__ == "__main__":
    result_1 = re.match(r'\d', '111111')
    print(result_1)

    result_2 = re.match(r'^\d{3}\-\d{3,8}$', '010-12345')
    print(result_2)

    s1 = 'a b    c'
    s2 = s1.split(' ')
    print(s2)
    s3 = re.split(r'\s+', s1)
    print(s3)

    # result_3 = re.match(r'^(\d{3})-(\d{3, 8})$', '010-12345')
    # print(result_3.group(0))
    # print(result_3.group(1))
    # print(result_3.group(2))

    result_4 = re.match(r'^(\d+)(0*)$', '102300')
    print(result_4)
    print(result_4.groups())
    print(result_4.group(0))
    print(result_4.group(1))
    print(result_4.group(2))
    # print(result_4.group(3))

    result_5 = re.match(r'^(\d+?)(0*)$', '102300')
    print(result_5)
    print(result_5.groups())
    print(result_5.group(0))
    print(result_5.group(1))
    print(result_5.group(2))

    regex_1 = re.compile(r'\w\w\d')
    result_6 = regex_1.match('AB2')
    print(result_6)
    
    result_7 = regex_1.match('A22')
    print(result_7)