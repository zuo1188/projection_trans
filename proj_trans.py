import pyproj

pUTM = pyproj.Proj(init= 'EPSG:32651')
pWGS84 = pyproj.Proj(init = 'EPSG:4326')
result = pyproj.transform(pWGS84,pUTM,120.25293698,31.46537104)
print(result)