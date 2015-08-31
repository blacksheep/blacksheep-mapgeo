import argparse
import bisect
import sys

class ZipCodes(object):
    def __init__(self):
        self.zips = []
    def load_from_file(self, fname):
        with open(fname, 'r') as f:
            for line in f.readlines():
                line = line.strip()
                items = [i.strip() for i in line.split(',')]
                bisect.insort_left(self.zips, (int(items[0]), items[1]))
    def find_greatequal_lessequal(self, greatequal, lessequal):
        return self.find_left_insert_pos(greatequal), self.find_left_insert_pos(lessequal)
    def find_left_insert_pos(self, val):
        return bisect.bisect_left(self.zips, (val,'zzzz'))


def parse_args(args):
    parser = argparse.ArgumentParser(description='Zip Radius Search')
    parser.add_argument('--zip', dest='zip', help='Zip Code', required=True)
    parser.add_argument('--greatequal', dest='greatequal', default=0, type=int, help='great equal than in meters')
    parser.add_argument('--lessequal', dest='lessequal', required=True, type=int, help='less equal than in meters')
    return parser.parse_args(args)

def main():
    targs = parse_args(sys.argv[1:])
    zip = ZipCodes()
    zip.load_from_file(targs.zip)
    lessequal = targs.lessequal
    greatequal = targs.greatequal
    ind1, ind2 = zip.find_greatequal_lessequal(greatequal, lessequal)
    print zip.zips[ind1:ind2]


if __name__ == '__main__':
    main()

#python search_file.py --zip 35004 --greatequal 40 --lessequal 150
