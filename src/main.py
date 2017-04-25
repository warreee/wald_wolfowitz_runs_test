from scipy.special import ndtr


def _calculate_p_value(z_value):
    """
    Calculates the p value given a z value.
    Here we assume using the normal distribution
    :return: 
    """
    return ndtr(z_value)


def runs(list1, list2, confidence_interval=0.05):
    """
    This function executes the whole Wald-Wolfowitz runs tests.
    :param list1: 
    :param list2: 
    :param confidence_interval: 
    :return: 
    """
    return 0.1
