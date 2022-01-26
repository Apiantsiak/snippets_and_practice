

class Subnet:

    def __init__(self, ip: str, prefix: str):
        self.ip = ip
        self.prefix = prefix

    # Prefix to binary wildcard

    @property
    def wildcard(self) -> str:
        """Convert prefix notation to binary wildcard

        :return: str
        """

        one_scope: int = 32 - int(self.prefix)
        binary_wildcard: str = "0" * int(self.prefix) + "1" * one_scope
        ls = list(binary_wildcard)

        for pos, _ in enumerate(ls):
            if pos in [8, 17, 26]:
                ls.insert(pos, ".")
        wild_card = "".join(ls)

        return wild_card

    # Prefix to binary subnet mask

    @property
    def cidr(self) -> str:
        """Convert prefix notation to binary subnet mask

        :return: str
        """

        zero_scope: int = 32 - int(self.prefix)
        binary_cidr: str = "1" * int(self.prefix) + "0" * zero_scope
        ls = list(binary_cidr)

        for pos, _ in enumerate(ls):
            if pos in [8, 17, 26]:
                ls.insert(pos, ".")
        cidr = "".join(ls)

        return cidr

    # Decimal to binary

    @staticmethod
    def binary(val: str) -> str:
        """Convert decimal to binary
        :param: str
        :return: str
        """

        ls_vals = val.split(".")
        bin_vals = [bin(int(val))[2:] for val in ls_vals]

        for pos, val in enumerate(bin_vals):
            if len(val) < 8:
                delta = 8 - len(val)
                zero = "0" * delta
                bin_vals.insert(pos, zero + bin_vals.pop(pos))
        binary_val = ".".join(bin_vals)

        return binary_val

    # Binary to Decimal

    @staticmethod
    def decimal(val: str) -> str:
        """Convert binary to decimal
        :param: str
        :return: str
        """

        ls_vals = val.split(".")
        decimal_vals = []

        for val in ls_vals:
            decimal_numb = 0
            for pos, char in enumerate(reversed(val)):
                if int(char):
                    decimal_numb += 2 ** pos
            decimal_vals.append(str(decimal_numb))
        decimal_val = ".".join(decimal_vals)

        return decimal_val

    # Network ID calculation

    @property
    def network_id(self) -> str:
        """Calculate network id (add together binary ip with cidr)
        using method 1 and 1 = 1 else 0

        :return: str
        """
        binary_ip = self.binary(self.ip)
        binary_cidr = self.cidr

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

    @property
    def host_number(self) -> str:
        """Calculate number IP using formula '2**(32-prefix)-2'

        :return: str
        """

        numbs_ip = str(2 ** (32 - int(self.prefix)) - 2)
        return numbs_ip


subnet = Subnet("192.168.156.3", "24")

t = '\t'*3

print(f"Network ID:{t}{subnet.decimal(subnet.network_id)}",
      f"CIDR:{t}\t{subnet.cidr}",
      f"Wildcard:{t}{subnet.wildcard}",
      f"Netmask:{t}{subnet.decimal(subnet.cidr)}",
      f"Number IP Address:\t{subnet.host_number}", sep="\n")
