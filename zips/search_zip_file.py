import argparse
import bisect
import sys
from pprint import pprint as pp
from geopy.distance import vincenty
import bisect
import time
import os.path


start_time = time.time()
errors = []
curr_dir = os.path.dirname(os.path.realpath(__file__))
zip_dir = 'zips'

class BSZip(object):
    def __init__(self):
        self.id = 0
        self.zip = ''
        self.state_abbr = ''
        self.state = ''
        self.city = ''
        self.latitude = 0
        self.longitude = 0
        self.neighbours = []
    def to_dict(self):
        return {'id':self.id,
                'zip':self.zip,
                'state_abbr':self.state_abbr,
                'state':self.state,
                'city':self.city,
                'latitude':self.latitude,
                'longitude':self.longitude,
                'neighbours':self.neighbours,
                }
    def load_neighbors_from_bszips(self, data, unit='m'):
        zip1 = self.zip
        for zip2 in data:
            # if zip1 != zip2:
                zip1_coord = (data[zip1].latitude, data[zip1].longitude)
                zip2_coord = (data[zip2].latitude, data[zip2].longitude)
                if unit=='mile':
                    distance = float(format(vincenty(zip1_coord, zip2_coord).miles, '.3f'))
                else:
                    distance = (int)(vincenty(zip1_coord, zip2_coord).m)
                item = (distance, zip2)
                bisect.insort_left(data[zip1].neighbours, item)

    def find_greatequal_lessequal(self, greatequal, lessequal):
        return self.find_left_insert_pos(greatequal), self.find_left_insert_pos(lessequal)

    def find_left_insert_pos(self, val):
        return bisect.bisect_left(self.neighbours, (val,'zzzz'))

    def __str__(self):
        return str(self.to_dict())
    def __repr__(self):
        return str(self.to_dict())

def load_from_string(lineNum, line, data={}):
    '''"zip code", "state abbreviation", "latitude", "longitude", "city", "state"
    "95035", "CA", " 37.436451", "-121.89438", "Milpitas", "California"
    '''
    try:
        zip = BSZip()
        items = [i.strip('" ') for i in line.split(',')]
        zip.id = lineNum
        zip.zip = items[0]
        zip.state_abbr= items[1]
        zip.state = items[5]
        zip.city = items[4]
        zip.latitude = float(items[2])
        zip.longitude = float(items[3])
        data[zip.zip] = zip
    except Exception as exc:
        print 'Line ' + str(lineNum) + ' '+ line + ': ' + str(exc)
        errors.append(lineNum)

def init_data(fname, data={}):
    with open(fname, 'r') as f:
        line = f.readline()
        for i, line in enumerate(f.readlines()):
            line = line.strip()
            if line:
                load_from_string(i, line, data)

def parse_args(args):
    parser = argparse.ArgumentParser(description='Zip Radius Search')
    parser.add_argument('--zip', dest='zip', help='Zip Code', required=True)
    parser.add_argument('--greatequal', dest='greatequal', default=0, type=int, help='great equal than in meters')
    #parser.add_argument('--great', dest='great', default=0, help='great than in meters')
    parser.add_argument('--lessequal', dest='lessequal', required=True, type=int, help='less equal than in meters')
    #parser.add_argument('--less', dest='less', help='less than in meters')
    parser.add_argument('--unit', dest='unit', default='m', choices=['m', 'mile'], help='less than in meters')
    return parser.parse_args(args)

def main():
    #print sys.argv
    targs = parse_args(sys.argv[1:])
    #print targs
    if targs.unit == 'm':
        greatequal = targs.greatequal - 1
        lessequal = targs.lessequal + 1
    else:
        greatequal = targs.greatequal - 0.001
        lessequal = targs.lessequal + 0.001

    fname = 'zips.csv'
    #fname = 'zips_simple.csv'
    data = {}
    init_data(fname, data)
    total = len(data)
    #print total

    try:
        data[targs.zip].load_neighbors_from_bszips(data, unit=targs.unit)
        ind1, ind2 = data[targs.zip].find_greatequal_lessequal(greatequal, lessequal)
        #print ind1, ind2, greatequal, lessequal
        print 'total:', ind2-ind1
        print data[targs.zip].neighbours[ind1:ind2]
    except KeyError as exc:
        print "KeyError: didn't find", str(exc)
    except Exception as exc:
        print 'Exception:', str(exc)


if __name__ == '__main__':
    main()

#python search_zip_file.py --zip 35004 --greatequal 40 --lessequal 150 --unit mile
#python search_zip_file.py --zip 35004 --greatequal 4000 --lessequal 15000 --unit m
