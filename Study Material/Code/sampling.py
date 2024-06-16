# -*- coding: utf-8 -*-


from scipy.stats import norm
print(1-norm.cdf(40, loc=36, scale=2))

#confidence interval for population mean, standard deviation unknown
from scipy.stats import t
import math
confidence = 0.95
m=12630
n=27
std_dev=5393
std_err=std_dev/math.sqrt(n)

h = std_err * t.ppf((1 + confidence) / 2, n - 1)

print( m - h)
print ( m + h)

#confidence interval for population mean, standard deviation known
m=792
n=25
alpha=0.05
std_err=15/math.sqrt(n)
zval=norm.ppf(1-alpha/2)
h1=std_err*zval

#h = std_err * t.ppf((1 + confidence) / 2, n - 1)
print(h1)

print( m - h1)
print ( m + h1)

#confidence interval for o proportion
prop=0.25
samp_size=24
me=zval*math.sqrt(prop*(1-prop)/samp_size)

print(prop+me)
print(prop-me)

#computing a prediction interval
m=12630.37
n=27
perr=t.ppf((1 + confidence) / 2, n - 1)*std_dev*math.sqrt(1+1/n)
print(m+perr)
print(m-perr)

#sample size determination for the mean
alpha=0.05
sd=15
n=97
m=796
err=3
print(math.pow(zval,2)*math.pow(sd,2)/math.pow(err,2))

#sample size determination for the proportion
alpha=0.05
sd=15
n=97
m=796
pi=0.5
err=0.02
print(math.pow(zval,2)*pi*(1-pi)/math.pow(err,2))

