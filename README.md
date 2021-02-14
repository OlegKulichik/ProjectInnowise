Project_innowise

1.Install GDAL for Python:

sudo add-apt-repository ppa:ubuntugis/ppa

sudo apt-get update

sudo apt-get install gdal-bin

sudo apt-get install libgdal-dev

export CPLUS_INCLUDE_PATH=/usr/include/gdal

export C_INCLUDE_PATH=/usr/include/gdal

pip install GDAL

2.Upgrade postgres to postgis:

sudo apt install postgis postgresql-postgis

CREATE EXTENSION postgis;