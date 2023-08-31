import numpy as np
import xarray as xr
import matplotlib.pyplot as pypl
import matplotlib.ticker as mticker
import cartopy
import cartopy.crs as crs


in_file = "CONDITIONS_v1.nc.999"
out_file = "result_CONDITIONS_v1.nc"
data = xr.open_dataset(in_file)

#dataArrTemp = xr.DataArray(, dims=('time', 'lat', 'lon'), name = 'GT_atm')

#print(data)

#data['GT_atm'] = data['GT_atm'].fillna(300.0)
#data['SICN_atm'] = data['SICN_atm'].fillna(0.0)
#data['SIC_atm'] = data['SIC_atm'].fillna(0.0)

data['GT_atm'] = data['GT_atm']*0.0+300.0
data['SICN_atm'] = data['SICN_atm']*0.0
data['SIC_atm'] = data['SIC_atm']*0.0


#for var_name, vari in data.variables.items():
#    if vari.dtype == np.float32:
#        data[var_name] = data[var_name].astype(np.float64)

data.to_netcdf(out_file, 'w')

dataOut = xr.open_dataset(out_file)

print(dataOut)
