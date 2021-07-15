class Test:
    public_num = 0
    __private_num = 1

if __name__ == "__main__":
    test = Test()
    print(test.public_num)
    print(test.__private_num)