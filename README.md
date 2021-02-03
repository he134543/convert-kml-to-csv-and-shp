# convert-kml-to-csv-and-shp
It is a python scipt to Convert kml file to csv and shp(polygon).
--
--
## Environment Setting
These scripts rely on numpy, gdal and pyshp. 
- pip install numpy
- pip install pyshp
- For gdal, it is tricky to get it installed. The best choice is to download the whl file from https://www.lfd.uci.edu/~gohlke/pythonlibs and install the package offline.
Or if you don't want to mess up with environmental setting. You can directly use the exe file(for Windows user).
--
--


## Which py file I need to use?
Because KML files created by different software has a bit difference, here I listed the py files dealing with output from omap and Google Earth Pro 


kml-csv.py and kml-shp-polygon.py are based on omap

google-kml-csv.py and google-kml-shp-polygon.py are based on Google Earth Pro


## How I get a csv or shp from the kml.
--
Run the kml-csv.py (or kml-shp-polygon.py), input your kml address and output dir you want to store the shp files.

## What if I don't want polygon?
Transoform your kml to csv. And import your csv file to QGIS. 
