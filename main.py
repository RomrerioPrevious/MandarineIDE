from bin.handlers.code_parser import CodeParser


def main():
    x = CodeParser("D:\g.py")
    print(x.parse_code())


if __name__ == "__main__":
    main()
