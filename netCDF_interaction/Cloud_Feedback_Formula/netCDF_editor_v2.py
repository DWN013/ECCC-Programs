import xarray as xr

in_file = "CONDITIONS_v1.nc.999"
out_file = "result_CONDITIONS_v2.nc"
data = xr.open_dataset(in_file)

GT_atm = data['GT_atm']
SICN_atm = data['SICN_atm']
SIC_atm = data['SIC_atm']

GT_atm_copy = GT_atm.copy()
SICN_atm_copy = SICN_atm.copy()
SIC_atm_copy = SIC_atm.copy()

GT_atm_copy[:] = 100.0

#for i in range (len(GT_atm_copy['lat'])):
#    print(i)


GT_atm_copy[:, 63, :] = 5.0

SICN_atm_copy[:] = 0.0
SIC_atm_copy[:] = 0.0

modified_ds = xr.Dataset({'GT_atm': GT_atm_copy, 'SICN_atm': SICN_atm_copy, 'SIC_atm': SIC_atm})

modified_ds.to_netcdf(out_file, 'w')

dataOut = xr.open_dataset(out_file)

print(dataOut)