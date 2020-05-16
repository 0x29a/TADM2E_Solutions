class BracketException(Exception):
    """
    Exception class for improperly nested parentheses string.
    """


def check_parentheses_nesting(string):
    stack = []

    for index, bracket in enumerate(string):
        if bracket not in {"(", ")"}:
            raise BracketException(f"'{bracket}' is not a valid character.")

        if bracket == "(":
            stack.append(str(index))
        elif bracket == ")":
            try:
                stack.pop()
            except IndexError:
                raise BracketException(
                    f"Closing bracket with index {index} is superfluous"
                )
    if stack:
        raise BracketException(
            f"Brackets with indexes {', '.join(stack)} are not closed."
        )


def main():
    valid_strings = ["((())())()", "()", "()()", "(((())))", "(" * 1000 + ")" * 1000]
    invalid_strings = [")()(", "())", "(" * 1000 + ")" * 1000 + ")"]

    for parentheses in valid_strings + invalid_strings:
        print(f"Checking {parentheses}:")
        try:
            check_parentheses_nesting(parentheses)
        except BracketException:
            print("Invalid")
        else:
            print("Valid")


if __name__ == "__main__":
    main()
