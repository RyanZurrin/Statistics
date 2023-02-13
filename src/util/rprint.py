# create a print function that prints like the python print function but also
# returns whatever it prints
import sys


def rprint(*args, **kwargs):
    sep = kwargs.get('sep', ' ')
    end = kwargs.get('end', '\n')
    file = kwargs.get('file', sys.stdout)
    output = sep.join([str(arg) for arg in args]) + end
    # check if it is numaric and if it is return a float
    file.write(output)
    try:
        output = float(output)
    except ValueError:
        pass
    return output
