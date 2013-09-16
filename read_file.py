import re
class FileReader:

    def readFile():
        f = open('ExpBindingEnergies.txt', "r")
        j = f.read()
        lines_array = re.findall(r'\d+\t\d+\t\d{1,}\.?\d+?', j)

        a_value = []
        z_value = []
        binding_energy = []


        for x in lines_array:
            a_value.append(x.split('\t')[0])
            z_value.append(x.split('\t')[1])
            binding_energy.append(x.split('\t')[2])


