import numpy as np
import matplotlib.pyplot as plt
from math import sin, pi, sqrt, exp


def loglogistic(arg, alp):
    nom = (beta/alp)*((arg/alp)**(beta-1))
    den = (1 + ((arg/alp)**beta))**2
    return nom/den


def alpha(mean):
    nom = mean*sin(pi/beta)
    den = pi/beta
    return nom/den

beta = 3.63
aboveave = 100
x = range(0, 1000)
y = []
z = [200.0, 250.0, 300.0, 400.0, 550.0]
integrate = []
for k in z:
    integrate.append(0)
    y.append([])
    for i in x:
        y[-1].append(loglogistic(i, alpha(k)))
        if i > k:
            integrate[-1] += y[-1][-1] * 100
        else:
            integrate[-1] -= y[-1][-1] * 100
            

fig, ax = plt.subplots()
plt.plot(x, y[0], color="r", label="{0:.1f} ave, {1:.2f}%".format(z[0],abs(integrate[0])))
plt.plot(x, y[1], color="b", label="{0:.1f} ave, {1:.2f}%".format(z[1],abs(integrate[1])))
plt.plot(x, y[2], color="g", label="{0:.1f} ave, {1:.2f}%".format(z[2],abs(integrate[2])))
plt.plot(x, y[3], color="k", label="{0:.1f} ave, {1:.2f}%".format(z[3],abs(integrate[3])))
plt.plot(x, y[4], color="c", label="{0:.1f} ave, {1:.2f}%".format(z[4],abs(integrate[4])))
plt.legend(bbox_to_anchor=(1.03, 1, 0, 0), loc=2, borderaxespad=0.)
fig.subplots_adjust(right=0.7)
plt.ylabel("Percentage of users %")
plt.xlabel("Minutes used")
plt.title("% of users using less mins than ave mins of the operator".format(aboveave))

print "ref 1 : Surprising Patterns for the Call Duration Distribution of \
        \nMobile Phone Users. Vaz de Melo1, Akoglu, Faloutsos, Loureiro"
print u"ref 2 : Call Duration Characteristics based on Customers Location. \u017Dvinys, Gur\u0161nys"


t = np.arange(0, 36, 0.1)
cost = [2.5, 5.0, 10.0, 15.0]
y = []
for i in cost:
    y.append([])
    for j in t:
        cnvfct = exp((0.5*(abs(integrate[0])/100)*j))
        lossgain = cnvfct*(exp(-((j-18+i)/(18))**2))
        #cnvfct = ((1+abs(integrate[0]/100)) * exp(-(i/50)**2)) + ((100 - abs(integrate[0]))/100 *exp(-((20-i)/50)**2))
        #cnvfct = - ((100 - abs(integrate[0]))/100 *exp(-((20-i)/100)**2))
        y[-1].append(lossgain)
        
fig, ax = plt.subplots()
plt.plot(t, y[0], color="r", label="cost {0:.1f}".format(cost[0]))
plt.plot(t, y[1], color="b", label="cost {0:.1f}".format(cost[1]))
plt.plot(t, y[2], color="g", label="cost {0:.1f}".format(cost[2]))
plt.plot(t, y[3], color="k", label="cost {0:.1f}".format(cost[3]))

plt.legend(bbox_to_anchor=(1.03, 1, 0, 0), loc=2, borderaxespad=0.)
fig.subplots_adjust(right=0.7)
plt.ylabel("Net Percentage of users converted")
plt.xlabel("Number of Months")
plt.title("Cost calculation(Log-Logistics model for ave 200mins)")

plt.show()
