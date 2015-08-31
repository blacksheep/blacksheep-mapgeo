# Steps to find zips from zips.csv based on the radius of zip code
1) create python virtual environment
2) pip install -r requests.txt

# search_zip_file.py: calculate the zip code based on its radius
3) python search_zip_file.py --zip 94089 --greatequal 40 --lessequal 150 --unit mile
4) python search_zip_file.py --zip 94089 --greatequal 4000 --lessequal 15000 --unit m


# zip.py: create folder zips, which has ~ 33000 files, each file name is a zip code
#  and it contains all the zip code in a sorted order based on the distance
5) python zip.py

# search_zip.py search the radius based on the zip files retrieved from zip.py
#  make sure the file exists, a simple demo file 62450 is included here
6) python search_file.py --zip 62450 --lessequal 50000 
