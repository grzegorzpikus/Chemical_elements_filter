import csv


def header(file):
    """Return the header of csv file"""
    with open(file) as infile:
        data = csv.reader(infile)
        category_list = next(data)
    return category_list


def reader(file, Class_name):
    """Reader of a csv file -> a dictionary"""
    with open(file) as infile:
        data = csv.DictReader(infile)

        dictionary_elements = {}
        mnm = ''
        for i in data:
            atomic_number = i['AtomicNumber']
            element = i['Element']
            symbol = i['Symbol']
            atomic_mass = i['AtomicMass']
            number_of_neutrons = i['NumberofNeutrons']
            period = i['Period']
            group = i['Group']
            phase = i['Phase']
            if i['Radioactive'] == 'Yes':
                radioactive = True
            else:
                radioactive = False
            if i['Metal'] == 'Yes' and i['Nonmetal'] != 'Yes' and i['Metalloid'] != 'Yes':
                mnm = 'metal'
            elif i['Metal'] != 'Yes' and i['Nonmetal'] == 'Yes' and i['Metalloid'] != 'Yes':
                mnm = 'nonmetal'
            elif i['Metal'] != 'Yes' and i['Nonmetal'] != 'Yes' and i['Metalloid'] == 'Yes':
                mnm = 'metalloid'
            type = i['Type']
            atomic_radius = i['AtomicRadius']
            electronegativity = i['Electronegativity']
            first_ionization = i['FirstIonization']
            melting_point = i['MeltingPoint']
            boiling_point = i['BoilingPoint']
            discoverer = i['Discoverer']
            year = i['Year']
            number_of_valence = i['NumberofValence']

            class_object = Class_name(atomic_number, element, symbol, atomic_mass, number_of_neutrons, period, group, phase, radioactive, mnm, type, atomic_radius, electronegativity, first_ionization, melting_point, boiling_point, discoverer, year, number_of_valence)

            dictionary_elements[atomic_number] = class_object

    return dictionary_elements


def test_function(file):
    with open(file) as infile:
        data = csv.DictReader(infile)
        next(data)
        print(next(data))