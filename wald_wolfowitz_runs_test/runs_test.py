from scipy.stats import norm
import numpy as np


def _calculate_p_value(z_value):
    """
    Calculates the p value given a z value.
    Here we assume using the normal distribution
    :return: 
    """
    return norm.sf(z_value)


def runs(list1, list2, confidence_interval=0.05):
    """
    This function executes the whole Wald-Wolfowitz runs tests.
    :param list1: 
    :param list2: 
    :return: 
    """
    labels = _get_runs_list(list1, list2)
    nruns = _calculate_nruns(labels)
    mean = _calculate_mean(len(list1), len(list2))
    variance = _calculate_variance(mean, len(list1) + len(list2))
    z_score = _calculate_z_score(nruns, mean, variance)
    p_val = _calculate_p_value(z_score)
    return p_val <= confidence_interval, p_val


def _get_runs_list(list1, list2):
    """
    Given the 2 lists create the runs list.
    i.e. label both lists and sort the concatenated lists and then return the list of labels
    :param list1: 
    :param list2: 
    :return: 
    """
    l1 = list(_add_label_to_list(list1, "X"))
    l2 = list(_add_label_to_list(list2, "Y"))
    lst = l1 + l2
    sorted_list = sorted(lst, key=lambda x: x[0])
    return [l[1] for l in sorted_list]


def _add_label_to_list(lst, label):
    """
    Given a list create a list of tuples of which the second element is the label.
    :param lst: 
    :param label: 
    :return: 
    """
    return map(lambda x: (x, label), lst)


def _calculate_z_score(nruns, mean, variance):
    """
    Calculates the z-score.
    :return: 
    """
    return (nruns - mean) / np.sqrt(variance)


def _calculate_mean(n_plus, n_min):
    """
    Calculates the mean, defined as:
    (2 * n_plus * n_min)/N + 1
    :param n_plus: 
    :param n_min: 
    :return: 
    """
    numerator = 2 * n_plus * n_min
    denominator = n_plus + n_min
    return numerator / float(denominator) + 1


def _calculate_variance(mean, n):
    """
    Calculates the variance
    :return: 
    """
    assert n > 1, "The number of elements should be higher than 1"
    return ((mean - 1) * (mean - 2)) / float(n - 1)


def _calculate_nruns(labels):
    """
    Calculate the number of runs.
    A run is defined as the follow up of the same signs.
    :return: int, the number of runs
    """
    nruns = 0
    last_seen = None

    for label in labels:
        if label != last_seen:
            nruns += 1
        last_seen = label

    return nruns
