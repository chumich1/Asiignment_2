import math
def calcBindingEnergy(a, z):
    avol = 15.85
    asur = 18.34
    acol = .71
    asym = 23.21
    ap = 12

    binding_energy = (avol*a - (asur*math.pow(a,2/3)) - (acol*z*(z-1)*math.pow(a, -1/3)) - (asym*math.pow(a-2*z, 2)/a))

    if(z%2 == 0 and (a-z)%2 == 0):
        binding_energy += ap*math.pow(a, -3/4)
    elif(z%2 == 1 and (a-z)%2 == 1):
        binding_energy -= ap*math.pow(a, -3/4)

    return binding_energy
    
print calcBindingEnergy(264,108)
