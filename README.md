# python_unittest
## Program structure
Unittest for Helvar code interview
CSV files contain synthetic data for testing which can be changed and scaled.

Test results are save in test_result.csv.

DUT and MEAS classes are separated in 2 files DUT.py and MEAS.py
Test class is saved in Helvar_test.py

Test condition is if all DUT values come with acceptable erro range compare with MEAS values.

## To run the test
Run in terminal
```buildoutcfg
clear
python Helvar_test.py
```
## In process work
Create Device class for inheritance of DUT and MEAS class -> reduce code duplication- 