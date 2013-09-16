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
def calcBindingEnergy2(a, z):
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

    return binding_energy

print calcBindingEnergy2(26 ,12)

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

ReadFile()
print calcBindingEnergy(2,1)
import matplotlib.pyplot as plt
plot1 = plt.plot(a_value, binding_per_nuc, 'bo')
plot2 = plt.plot(a_value, liquidDropEnergies(), 'ro')
plt.setp(plot1, label="")

plt.ylabel('Binding Energy [MeV/Nucleon]')
plt.xlabel('Number of Nucleons')
plt.show()


