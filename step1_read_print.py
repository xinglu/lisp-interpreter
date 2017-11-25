import reader
import printer


def READ(string):
    return reader.read_str(string)


def EVAL(ast):
    return ast


def PRINT(ast):
    return printer.pr_str(ast)


def rep():
    while True:
        try:
            print(PRINT(EVAL(READ(input("user> ")))))
        except Exception as e:
            print(e)

if __name__ == '__main__':
    rep()