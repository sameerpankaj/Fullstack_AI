#Conduct T-Tests

#Perform one-sample, two-sample, paired tests

#One Sample T-Test

from scipy.stats import ttest_1samp, ttest_ind, ttest_rel

##One Sample T-Test 
#Data set
data = [12, 14, 15, 16, 17]
population_mean = 15
ttest_1samp(data, population_mean)
t_stat, p_value =ttest_1samp(data, population_mean)
print('One Sample Test: \n', t_stat, p_value)



##Two Sample T-Test 
#Data set
group1 = [12, 14, 15, 16, 17]
group2 = [11, 13, 14, 15, 16]
t_stat, p_value = ttest_ind(group1, group2)
print('Two Sample Test: \n', t_stat, p_value)

#Paired Test
#Data Set
pre_test = [12, 14, 15, 16, 17]
post_test = [13, 14, 16, 17, 18]
t_stat, p_value = ttest_rel(pre_test, post_test)
print('Paired Test: \n', t_stat, p_value)



