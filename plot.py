import re



a_value = []
z_value = []
binding_energy = []
binding_per_nuc = []
binding_liq_drop = []

def ReadFile():
        f = open('ExpBindingEnergies.txt', "r")
        j = f.read()
        lines_array = re.findall(r'\d+\t\d+\t\d{1,}\.?\d+?', j)

        for x in lines_array:
            
            a_value.append(float(x.split('\t')[0]))
            z_value.append(float(x.split('\t')[1]))
            binding_energy.append(float(x.split('\t')[2])/1000)
            binding_per_nuc.append((float(x.split('\t')[2])/1000)/(float(x.split('\t')[0])))
          

 
import math
def calcBindingEnergy(a, z):
    avol = 15.85
    asur = 18.34
    acol = .71
    asym = 23.21
    ap = 12.0

    binding_energy = (avol*a - (asur*math.pow(a,2.0/3.0)) - (acol*z*(z-1)/math.pow(a, 1.0/3.0)) - (asym*math.pow(a-2.0*z, 2.0)/a))
   
    if(z%2 == 0 and (a-z)%2 == 0):
        binding_energy += ap/math.pow(a, 3.0/4.0)
    elif(z%2 == 1 and (a-z)%2 == 1):
        binding_energy -= ap/math.pow(a, 3.0/4.0)

    return binding_energy/a

def liquidDropEnergies():
    temp = 0
    while temp < len(a_value):
        binding_liq_drop.append(calcBindingEnergy(a_value[temp], z_value[temp]))
        temp+=1
        
    return binding_liq_drop

def subtractLists(list1, list2):
    new_list = []
    if(len(list1) == len(list2)):
        temp = 0
        while temp < len(list1):
            new_list.append((list1[temp] - list2[temp])*a_value[temp])
            temp+=1
    return new_list

ReadFile()
index28 = z_value.index(28)
index50 = z_value.index(50)
index82 = z_value.index(82)

import matplotlib.pyplot as plt
subtracted_list = subtractLists(binding_per_nuc, liquidDropEnergies())
plot1 = plt.plot(z_value, subtracted_list , 'bo')
plot1 = plt.plot([z_value[index28],z_value[index50],z_value[index82]] ,[subtracted_list[index28],subtracted_list[index50],subtracted_list[index82]] , 'ro')



plt.ylabel('(Measured - Calculated Binding Energy ) * A [MeV]')
plt.xlabel('Number of Protons')
plt.show()
