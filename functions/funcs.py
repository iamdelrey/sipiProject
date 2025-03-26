"""Contains utils for project"""


def is_float(num: int) -> bool:
    """This function validates float number

    :param num: number to validate
    :type num: int
    :return true if float otherwise false
    :rtype bool
    """
    try:
        float(num)
        return True
    except ValueError:
        return False
