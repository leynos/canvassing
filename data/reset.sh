#!/bin/bash
dropdb ssp_canvassing; createdb ssp_canvassing; psql ssp_canvassing -c "CREATE EXTENSION postgis;"
./manage.py syncdb --noinput
./manage.py fill_up_db data/postcodes3.csv
./manage.py load_wards data/Wards_GB_2014_Boundaries/WD_DEC_2014_GB_BFE.shp
./manage.py load_regions data/bdline_gb/Data/scotland_and_wales_const_region.shp data/bdline_gb/Data/scotland_and_wales_region_region.shp data/bdline_gb/Data/westminster_const_region.shp
./manage.py add_from_csv_dundee data/pp20_28-08-2014_MARKED-UP_1.csv