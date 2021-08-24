from Reader import reader, header, test_function
from Extractor import element_creator
from Element import Element




if __name__ == "__main__":
    elements = reader('Periodic Table of Elements.csv', Element)
    header('Periodic Table of Elements.csv')
    print(header('Periodic Table of Elements.csv'))
    print()
    test_function('Periodic Table of Elements.csv')
    print()
    print(elements)
    print()
    print(elements['1'])