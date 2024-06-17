import argparse

parser = argparse.ArgumentParser()
requiredNamed = parser.add_argument_group('required named arguments')
requiredNamed.add_argument('-m1', type=str, nargs='?', required=True,
                           help='name of the .gro file containing the fixed molecule')
requiredNamed.add_argument('-m2', type=str, nargs='?', required=True,
                           help='name of the .gro file containing the mobile molecule')
requiredNamed.add_argument('-origingrid', metavar='og', type=str, nargs='?', required=True,
                           help='name of the rotation grid for rotations around origin in the form '
                                'algorithm_N (eg. ico_50) OR just a number (eg. 50)')
requiredNamed.add_argument('-bodygrid', metavar='bg', type=str, nargs='?', required=True,
                           help='name of the rotation grid for rotations around body in the form '
                                'algorithm_N (eg. ico_50) OR just a number (eg. 50) '
                                'OR None if you only want rotations about origin')
requiredNamed.add_argument('-transgrid', metavar='tg', type=str, nargs='?', required=True,
                           help='translation grid provided as a list of distances, as linspace(start, stop, num) '
                                'or range(start, stop, step) in nanometers')
parser.add_argument('--recalculate', action='store_true',
                    help='recalculate the grid even if a saved version already exists')

def run_generate_pt():
    my_args = parser.parse_args()
    print(f"A run with args {my_args.m1} {my_args.m2} {my_args.recalculate} {my_args.bodygrid} {my_args.origingrid} {my_args.transgrid}")


if __name__ == '__main__':
    print("Running python")
    run_generate_pt()