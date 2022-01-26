

from typing import List


DECIMAL_IP: str = "192.168.156.3"
PREFIX: str = "21"


# CIDR notation to binary subnet mask


def prefix_to_cidr(cidr: str) -> str:
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


# Decimal to binary


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


# Network ID calculation


def network_id_func(binary_ip: str, binary_cidr: str) -> str:
    """Calculate network id (add together binary ip with cidr)
    using method 1 and 1 = 1 else 0

    :param binary_ip: str
    :param binary_cidr: str
    :return: str
    """

    network_id_ls = []
    for pos in range(len(binary_ip)):
        if binary_ip[pos] == ".":
            network_id_ls.append(".")
        elif int(binary_ip[pos]) and int(binary_cidr[pos]):
            network_id_ls.append("1")
        else:
            network_id_ls.append("0")

    bin_network_id = "".join(network_id_ls)

    return bin_network_id


# Number IP addresses


def calculate_numb_ip(prefix: str) -> str:
    """Calculate number IP using formula '2**(32-prefix)-2'

    :param prefix: str
    :return: str
    """

    numbs_ip = str(2 ** (32 - int(prefix)) - 2)
    return numbs_ip


bin_cidr: str = prefix_to_cidr(PREFIX)
bin_ip: str = decimal_to_binary(DECIMAL_IP)
dec_sub_mask: str = binary_to_decimal(bin_cidr)

print(bin_ip, bin_cidr, dec_sub_mask, sep="\n")
print(binary_to_decimal(network_id_func(bin_ip, bin_cidr)), PREFIX, sep="/")
