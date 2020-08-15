import pandas as pd
# Function for flattening json
# Source: https://www.geeksforgeeks.org/flattening-json-objects-in-python/
# https://medium.com/@augustin.goudet/introduction-to-finnhub-97c2117dd9a9

def flatten_json(y):
    out = {}
    def flatten(x, name =''):

        # If the Nested key-value
        # pair is of dict type
        if type(x) is dict:

            for a in x:
                flatten(x[a], name + a + '_')

                # If the Nested key-value
        # pair is of list type
        elif type(x) is list:

            i = 0

            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x

    flatten(y)
    return out

