import unittest

from MEAS import *
from DUT import *


# Compare if DUT value is in acceptable range, err range given in % (eg: err_range = 5)
def is_acceptable_value(DUT_val, MEAS_val, err_range):
    return (100 - err_range) * MEAS_val / 100 < DUT_val < (100 + err_range) * MEAS_val / 100


class Helvar_test(unittest.TestCase):
    def setUp(self):
        print("Set up")
        self.MEAS_list = create_MEAS_list()
        self.DUT_list = create_DUT_list()
        self.assertEqual(len(self.MEAS_list), len(self.DUT_list))

# Compare DUT values with MEAS value, save result to file
    def test_err_range(self):
        try:
            f = open("test_result.csv", "w")
        except FileNotFoundError:
            print("Error in creating the file, File not found!")
        else:
            passed_test = 0
            f.write("Name;DUT_current;MEAS_current;DUT_voltage;MEAS_voltage;Result\n")
            for i in range(len(self.MEAS_list)):
                accepted_voltage = is_acceptable_value(self.DUT_list[i].get_voltage(),
                                                       self.MEAS_list[i].get_voltage(),
                                                       5)
                accepted_current = is_acceptable_value(self.DUT_list[i].get_current(),
                                                       self.MEAS_list[i].get_current(),
                                                       5)
                if accepted_current and accepted_voltage:
                    f.write("{:s};{:.2f};{:.2f};{:.2f};{:.2f};{:s}\n".format(
                        self.DUT_list[i].get_name(),
                        self.DUT_list[i].get_current(),
                        self.MEAS_list[i].get_current(),
                        self.DUT_list[i].get_voltage(),
                        self.MEAS_list[i].get_voltage(),
                        "PASS"
                    ))
                    passed_test = passed_test + 1
                else:
                    f.write("{:s};{:.2f};{:.2f};{:.2f};{:.2f};{:s}\n".format(
                        self.DUT_list[i].get_name(),
                        self.DUT_list[i].get_current(),
                        self.MEAS_list[i].get_current(),
                        self.DUT_list[i].get_voltage(),
                        self.MEAS_list[i].get_voltage(),
                        "FAIL"
                    ))
            f.close()

        self.assertEqual(passed_test, len(self.DUT_list), "Not all values are in acceptable range")



if __name__ == '__main__':
    unittest.main()
