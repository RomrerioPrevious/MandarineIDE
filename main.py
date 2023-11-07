from bin.handlers.code_parser import CodeParser


def main():
    x = CodeParser("D://Save//MandarinIDE//tests//any_directory//1.py")
    print(x.parse_code())


if __name__ == "__main__":
    main()
