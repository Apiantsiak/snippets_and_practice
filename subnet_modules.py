

from typing import List

# Decimal to binary


DECIMAL_IP: str = "192.168.156.3"
CIDR: str = "32"


def cidr_to_binary(cidr: str) -> str:
    """Convert CIDR notation to binary subnet mask
    :param cidr: str
    :return: str
    """
    zero_scope: int = 32 - int(cidr)
    binary_cidr: str = "1" * int(cidr) + "0" * zero_scope
    ls = list(binary_cidr)
    for pos, _ in enumerate(ls):
        if pos in [8, 17, 26]:
            ls.insert(pos, ".")
    binary_cidr = "".join(ls)
    return binary_cidr


def decimal_to_binary(decimal_ip: str) -> str:
    """Convert decimal to binary
    :param decimal_ip: str
    :return: str
    """

    ls_vals: List[str] = decimal_ip.split(".")
    bin_vals = [bin(int(val))[2:] for val in ls_vals]

    for pos, val in enumerate(bin_vals):
        if len(val) < 8:
            delta = 8 - len(val)
            zero = "0" * delta
            bin_vals.insert(pos, zero + bin_vals.pop(pos))
    binary_ip = ".".join(bin_vals)

    return binary_ip


BINARY_IP: str = decimal_to_binary(DECIMAL_IP)


# Binary to Decimal


def binary_to_decimal(binary_ip: str) -> str:
    """Convert binary to decimal
    :param binary_ip: str
    :return: str
    """

    ls_vals: List[str] = binary_ip.split(".")
    decimal_vals = []

    for val in ls_vals:
        decimal_numb = 0
        for pos, char in enumerate(reversed(val)):
            if int(char):
                decimal_numb += 2 ** pos
        decimal_vals.append(str(decimal_numb))
    decimal_ip = ".".join(decimal_vals)

    return decimal_ip


print(BINARY_IP)
print(binary_to_decimal(BINARY_IP))
print(cidr_to_binary(CIDR))
print(binary_to_decimal(cidr_to_binary(CIDR)))
