class Element:

    def __init__(self, atomic_number, element, symbol, atomic_mass, number_of_neutrons, period, group, phase,
                 radioactive, mnm, type, atomic_radius, electronegativity, first_ionization, melting_point,
                 boiling_point, discoverer, year, number_of_valence):

        self.atomic_number = atomic_number
        self.element = element
        self.symbol = symbol
        self.atomic_mass = atomic_mass
        self.number_of_neutrons = number_of_neutrons
        self.period = period
        self.group = group
        self.phase = phase
        self.radioactive = radioactive
        self.mnm = mnm
        self.type = type
        self.atomic_radius = atomic_radius
        self.electronegativity = electronegativity
        self.first_ionization = first_ionization
        self.melting_point = melting_point
        self.boiling_point = boiling_point
        self.discoverer = discoverer
        self.year = year
        self.number_of_valence = number_of_valence

        # answer for radioactivity
        if self.radioactive is True:
            self.radioactive_answer = 'is radioactive'
        else:
            self.radioactive_answer = 'is not radioactive'

        # answer for metal/nonmetal/metaloid
        if self.mnm == 'Metal':
            self.mnm_answer = 'is metal'
        elif self.mnm == 'Nonmetal':
            self.mnm_answer = 'is nonmetal'
        else:
            self.mnm_answer = 'is metaloid'

        # history
        if self.discoverer == 'Prehistoric':
            self.history = ''
        elif self.discoverer == 'Early historic times':
            self.history = ''
        elif self.discoverer != '' and self.year != '':
            self.history = f'The element was discovered in {self.year}'
        else:
            self.history = f'The element was discovered by {self.discoverer} in {self.year}.'

    def __str__(self):
        return f"Atomic number of {self.element}/({self.symbol}) is {self.atomic_number}. The atomic mass of" \
               f"this element is {self.atomic_mass} u. The nucleus of {self.symbol} contains {self.atomic_number}" \
               f" protons {self.number_of_neutrons} nautorns. The element is located in the period no. " \
               f"{self.period}, in the group no. {self.group} and belongs to the group of {self.type}. This " \
               f"{self.mnm_answer} as a pure copound it is {self.phase} under normal conditions and " \
               f"{self.radioactive_answer}. The most common properties are as follow: atomic radius " \
               f"{self.atomic_radius} Å, lectronegativity {self.electronegativity}, first ionization" \
               f"{self.first_ionization}, melting point {self.melting_point} °C, boiling point {self.boiling_point} °C, " \
               f"number_of_valence {self.number_of_valence}. {self.history}"

    def __repr__(self):
        return self.element
