class DUT:
    def __init__(self, name, voltage, current):
        self.__name = name
        self.__voltage = voltage
        self.__current = current

    # Get name, voltage and values from DUT object
    def get_name(self):
        return self.__name

    def get_voltage(self):
        return self.__voltage

    def get_current(self):
        return self.__voltage

    # Set/Update voltage and values
    def set_voltage(self, voltage):
        self.__voltage = voltage

    def set_current(self, current):
        self.__current = current

    # Display a MEAS object:
    def __str__(self):
        return "DUT Device: {:s} | Current: {:.2f}mA | Voltage: {:.2f}V" \
            .format(self.__name, self.__current, self.__voltage)


def is_correct_form(s):
    return len(s.split(";")) == 3


# Read DUT information from csv file
def create_DUT_list():
    temp_data = []
    try:
        infile = open("DUT_values.csv", 'r')
    except FileNotFoundError:
        # print("There was an error in reading the input file!")
        print("Error in reading the file, File not found!")
    else:
        for line in infile:
            try:
                if not is_correct_form(line):
                    raise ValueError
            except ValueError as e:
                print("Error in reading the file , Not correct form!")
            else:
                if line.split(";")[0] == 'Name':
                    continue
                else:
                    name, current, voltage = line.split(";")
                    data = DUT(name, float(current), float(voltage))
                    temp_data.append(data)
        infile.close()
    return temp_data