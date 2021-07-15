import argparse

if __name__ == "__main__":
    my_parser = argparse.ArgumentParser(description="Help Information")
    my_parser.add_argument("arg1", type=str, help="The first argument")
    my_args = my_parser.parse_args()

    print(my_args.arg1)