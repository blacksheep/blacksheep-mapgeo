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

def write_to_file(data, zip):
    fname = os.path.join(curr_dir, zip_dir, zip)
    with open(fname, 'w') as f:
        zip_neighbors = data[zip].neighbours
        for distance, neighbour_zip in zip_neighbors:
            f.write(str(distance))
            f.write(', ')
            f.write(neighbour_zip)
            f.write('\n')

def main():
    fname = 'zips.csv'
    #fname = 'zips_simple.csv'
    data = {}
    new_zip_dir = os.path.join(curr_dir, zip_dir)
    if not os.path.exists(new_zip_dir):
        os.makedirs(new_zip_dir)
    print new_zip_dir
    print '------------------Now Init Data----------------'
    init_data(fname, data)
    print '------------------Now Calculation----------------'
    total = len(data)
    cnt = 0
    for zip1 in data:
        elapsed_time = time.time() - start_time
        print elapsed_time, 'cal-----' + str(total) + '(' + str(cnt) +')--------' +str(zip1)+'---------------'
        for zip2 in data:
            if zip1 != zip2:
                zip1_coord = (data[zip1].latitude, data[zip1].longitude)
                zip2_coord = (data[zip2].latitude, data[zip2].longitude)
                distance = (int)(vincenty(zip1_coord, zip2_coord).m)
                item = (distance, zip2)
                bisect.insort_left(data[zip1].neighbours, item)
        print '------------------Now Write To File----------------'
        elapsed_time = time.time() - start_time
        print elapsed_time, 'write----' + str(total) + '(' + str(cnt) +')--------' +str(zip1)+'---------------'
        write_to_file(data, zip1)
        data[zip1].neighbours = []
        cnt += 1
    print 'cnt:', cnt

    print 'Total Error:', len(errors)

if __name__ == '__main__':
    main()

