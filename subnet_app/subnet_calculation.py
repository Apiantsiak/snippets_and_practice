"""This module includes all the necessary methods and functions
to calculate subnet attributes from IP address and prefix"""


def convert_to_bin(decimal_val: str) -> str:
    """Convert decimal number to binary value

    :param decimal_val: str
    :return: str
    """
    binary_val_ls = [bin(int(val))[2:] for val in decimal_val.split(".")]

    for pos, val in enumerate(binary_val_ls):
        if len(val) < 8:
            zero_scope = 8 - len(val)
            binary_val_ls.insert(pos, "0" * zero_scope + binary_val_ls.pop(pos))

    binary_val = ".".join(binary_val_ls)

    return binary_val


def convert_to_dec(binary_val: str) -> str:
    """Convert binary value to decimal number

    :param binary_val:
    :return:
    """
    binary_vals_ls = binary_val.split(".")
    decimal_vals = []

    for item in binary_vals_ls:
        decimal_numb = 0
        for pos, val in enumerate(reversed(item)):
            if int(val):
                decimal_numb += 2 ** pos
        decimal_vals.append(str(decimal_numb))
    decimal_val = ".".join(decimal_vals)

    return decimal_val


class Subnet:

    SUBNET_INFO = {}

    def __init__(self, subnet_ip: str, prefix: str) -> None:
        self._ip = subnet_ip
        self._prefix = prefix
        self._address = f"{subnet_ip}/{prefix}"

    @property
    def ip(self) -> str:
        return self._ip

    @property
    def prefix(self) -> str:
        return self._prefix

    @property
    def address(self) -> str:
        return self._address

    @property
    def cidr(self, total_numb_bits: int = 32) -> str:
        """Convert prefix to classless inter-domain routing (cidr) binary value

        :param total_numb_bits: str
        :return: str
        """
        host_bits = total_numb_bits - int(self.prefix)
        subnet_mask_bin = ["1" for _ in range(int(self.prefix))]
        subnet_mask_bin.extend(["0" for _ in range(host_bits)])

        for pos, _ in enumerate(range(total_numb_bits)):
            if pos in [8, 17, 26]:
                subnet_mask_bin.insert(pos, ".")

        subnet_mask_bin = "".join(subnet_mask_bin)

        return subnet_mask_bin

    @property
    def wildcard(self) -> str:
        """Calculate wildcard value using cidr binary value

        :return: str
        """
        subnet_mask_ls = self.cidr.split(".")

        wildcard_ls = []
        for part in subnet_mask_ls:
            wildcard_part = ""
            for val in list(part):
                if int(val):
                    wildcard_part += "0"
                else:
                    wildcard_part += "1"
            wildcard_ls.append(wildcard_part)

        wildcard_bin = ".".join(wildcard_ls)

        return wildcard_bin

    @property
    def network_id(self) -> str:
        """Calculate subnet IP address and convert it to decimal interpretation

        :return: str
        """
        binary_ip = convert_to_bin(self.ip)
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

        return convert_to_dec(bin_network_id)

    @property
    def broadcast_ip(self) -> str:
        """Calculate last IP address of a subnet

        :return: str
        """
        net_dec_vals = self.network_id.split(".")
        wildcard_dec_vals = convert_to_dec(self.wildcard).split(".")

        broadcast_dec_vals = [str(int(net_val) + int(wildcard_dec_vals[pos]))
                              for pos, net_val in enumerate(net_dec_vals)
                              ]

        broadcast_ip = ".".join(broadcast_dec_vals)

        return broadcast_ip

    @property
    def next_network_id(self) -> str:
        """Calculate IP address of a next subnet

        :return: str
        """
        broad_vals = self.broadcast_ip.split(".")

        next_net_vals = []
        for broad_val in broad_vals:
            if broad_val == "255":
                next_net_vals.append("0")
            else:
                next_net_vals.append(broad_val)

        next_net_id = ".".join(next_net_vals)

        return next_net_id

    @property
    def first_sub_ip(self) -> str:
        """Calculate IP address after the network ID

        :return: str
        """
        net_vals = self.network_id.split(".")
        reserved_ip = "0.0.0.1"

        first_ip_vals = [str(int(net_val) + int(reserved_ip.split(".")[pos]))
                         for pos, net_val in enumerate(net_vals)
                         ]

        first_ip = ".".join(first_ip_vals)

        return first_ip

    @property
    def last_sub_ip(self) -> str:
        """Calculate IP address before the broadcast IP

        :return: str
        """
        broad_vals = self.broadcast_ip.split(".")
        reserved_ip = "0.0.0.1"
        last_ip_vals = [str(int(broad_val) - int(reserved_ip.split(".")[pos]))
                        for pos, broad_val in enumerate(broad_vals)
                        ]

        last_ip = ".".join(last_ip_vals)

        return last_ip

    @property
    def hosts_numb(self) -> str:
        """Calculate number of allocatable IP addresses

        :return: str
        """
        hosts = str(2 ** (32 - int(self.prefix)) - 2)

        return hosts

    def calculate(self, print_out: str = None) -> None:
        """Calculate and organize all subnet attributes into a dictionary
        and output them if the "print_out" attribute is equal to "p"

        :param print_out: str
        :return: None
        """
        if len(self.SUBNET_INFO) > 5:
            self.SUBNET_INFO.clear()

        self.SUBNET_INFO[self.address] = {}
        self.SUBNET_INFO[self.address]["Network ID"] = f"{self.network_id}/{self.prefix}"
        self.SUBNET_INFO[self.address]["Netmask/CIDR"] = f"{convert_to_dec(self.cidr)}/{self.cidr}"
        self.SUBNET_INFO[self.address]["Wildcard"] = f"{convert_to_dec(self.wildcard)}/{self.wildcard}"
        self.SUBNET_INFO[self.address]["Broadcast IP"] = self.broadcast_ip
        self.SUBNET_INFO[self.address]["First IP"] = self.first_sub_ip
        self.SUBNET_INFO[self.address]["Last IP"] = self.last_sub_ip
        self.SUBNET_INFO[self.address]["Next Network ID"] = self.next_network_id
        self.SUBNET_INFO[self.address]["Hosts"] = "{:,}".format(int(self.hosts_numb))

        if print_out == "p":
            print(f"\n{self.address} attributes:\n")
            for key, val in self.SUBNET_INFO[self._address].items():
                print(f"{key}:{' ' * (16 - len(key))}{val}")


if __name__ == "__main__":
    SUBNET_IP: str = "192.168.156.3"
    PREFIX: str = "10"
    sub = Subnet(SUBNET_IP, PREFIX)
    sub.calculate()
    print(list(sub.SUBNET_INFO[sub.address].items()))
