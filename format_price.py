import re, sys


def format_price(price):
    price_match = re.fullmatch(r"([\d]{1,10})(\.[\d]{1,6})?", price)
    if price_match is None:
        return None

    aparted_price = price_match.groups()

    integer_part = int(aparted_price[0])

    if aparted_price[1] is not None:
        fractional_part = int(aparted_price[1].replace(".", "")[:2])
    else:
        fractional_part = 0

    if fractional_part == 0 :
        return "{:,}".format(integer_part).replace(",", " ")

    return "{:,}.{:02}".format(integer_part, fractional_part).replace(",", " ")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Put price string as parameter")
        exit(1)

    formatted_price = format_price(sys.argv[1])
    if formatted_price is None:
        print("Invalid price string")
        exit(1)

    print(formatted_price)
