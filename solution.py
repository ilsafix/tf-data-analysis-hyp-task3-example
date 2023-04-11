import pandas as pd
import numpy as np
from scipy.stats import ttest_ind

chat_id = 391223586 # Ваш chat ID, не меняйте название переменной

def solution(control_npv, test_npv) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    alpha = 0.04
    # calculate the sample means and standard deviations
    control_mean = np.mean(control_npv)
    test_mean = np.mean(test_npv)
    control_std = np.std(control_npv, ddof=1)
    test_std = np.std(test_npv, ddof=1)

    # calculate the t-statistic and p-value
    t, p = ttest_ind(test_npv, control_npv, equal_var=False)

    # calculate the degrees of freedom
    df = len(control_npv) + len(test_npv) - 2

    # calculate the critical t-value for the given significance level
    t_crit = np.abs(ttest_ind(control_npv, test_npv)[0])
    t_dist = t(df=df)
    t_dist_alpha = t_dist.ppf(1 - alpha)
    reject_null = t_crit > t_dist_alpha
