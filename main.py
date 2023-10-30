from bin.handlers.code_parser import CodeParser


def main():
    x = CodeParser("")
    print(x.parse_code())


if __name__ == "__main__":
    main()
