import numpy as np
import xarray as xr
import matplotlib.pyplot as pypl
import matplotlib.ticker as mticker
import cartopy
import cartopy.crs as crs


in_file = "td_p2-pictrl_555001-569912_monthly_clim_bc_v1.nc.999"
out_file = "result_CONDITIONS_v1.nc"
data = xr.open_dataset(in_file)

#print(data)

# The quick and ugly way if I just want constant values.
# This won't work well for GT_atm that varies with latitude.

data['GT_atm'] = data['GT_atm']*0.0+300.0
data['SICN_atm'] = data['SICN_atm']*0.0
data['SIC_atm'] = data['SIC_atm']*0.0

data.to_netcdf(out_file, 'w')

#dataOut = xr.open_dataset(out_file)

#print(dataOut)
