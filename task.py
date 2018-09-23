import argparse
from HW5 import rg

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', required=True, type=int, help='Range')
    parser.add_argument('-k', required=True, type=int, help='Tries')
    result = parser.parse_args()
    print(rg(result.n, result.k))
