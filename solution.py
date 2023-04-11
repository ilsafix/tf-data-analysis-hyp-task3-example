import pandas as pd
import numpy as np
from scipy.stats import t

chat_id = 391223586 # Ваш chat ID, не меняйте название переменной

def solution(control_sample, test_sample) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    alpha = 0.04
    n1 = len(control_sample)
    n2 = len(test_sample)
    x1_bar = np.sum(control_sample) / n1
    x2_bar = mp.sum(test_sample) / n2
    s1 = np.sum([(x - x1_bar)**2 for x in control_sample]) / (n1 - 1)
    s2 = np.sum([(x - x2_bar)**2 for x in test_sample]) / (n2 - 1)
    sp = ((n1 - 1) * s1 + (n2 - 1) * s2) / (n1 + n2 - 2)
    t_statistic = (x2_bar - x1_bar) / (sp * (1/n1 + 1/n2)**0.5)
    t_critical = t.ppf(1 - alpha/2, n1 + n2 - 2)
    return np.abs(t_statistic) > t_critical
