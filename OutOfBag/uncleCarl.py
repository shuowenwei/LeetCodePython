

# about HbA1c test: https://medlineplus.gov/lab-tests/hemoglobin-a1c-hba1c-test/

# examples 
data = [{'A1C_INDEX': 5.5,
         'other_keys1': 1,
         'other_keys2': 'other_values2',
         },
        {'A1C_INDEX': 6.0,
         'other_keys1': 1,
         'other_keys2': 'other_values2',
         },
        {'A1C_INDEX': 5.5,
         'other_keys1': 1,
         'other_keys2': 'other_values2',
         },
        {'A1C_INDEX_DOES_NOT_EXIST': 5.5,
         'other_keys1': 1,
         'other_keys2': 'other_values2',
         },
        {'A1C_INDEX': 7.5,
         'other_keys1': 1,
         'other_keys2': 'other_values2',
         },
        {'A1C_INDEX': 10.5,
         'other_keys1': 1,
         'other_keys2': 'other_values2',
         },
        ]
num_quarters = 8
assert num_quarters >= len(data), 'Error: num_quarters must be greater or equal to length of \'data\' array'

import numpy as np
A1C_INDEX = 'A1C_INDEX'
def target_a1c(data):
    out = np.zeros(num_quarters, dtype = int)
    for i, x in enumerate(data): # i is the index of list data, starting from 0 to len(data)-1, x is the element, dictionary datatype
        for k, v in x.items(): # traverse through dictionary 'x' since it's dictionary format
            if k == A1C_INDEX: # for simplicity, just set A1C_INDEX to 'A1C_INDEX'
                value = float(v) # just in case 'v' is string or other format
                if value <= 5.7:
                    out[i] = 1
                elif value <= 6.4:
                    out[i] = 2
                elif value <= 9:
                    out[i] = 3
                else: # this is when 'value' > 9
                    out[i] = 4
    return out.tolist()

print(f'out is: {target_a1c(data)}')
# when num_quarters is greater than length of 'data' list, the default value is 0, in this case, it's the last two values in 'out'
# out is: [1, 2, 1, 3, 4, 0, 0]