
SUBNET: str = "192.168.152.3"
PREFIX: str = "24"


def network_id(subnet_ip: str, prefix: str):
    """Convert subnet with prefix in to network id

    :param subnet_ip: str
    :param prefix: str
    :return: str
    """
    network_id_value = f"{subnet_ip}/{prefix}"

    return network_id_value


print(network_id(SUBNET, PREFIX))
