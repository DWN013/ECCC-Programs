# A. Ukhin - July 12, 2023
# Average Ozone Calculation for Aquaplanet config
# This script create an average over all time values for some specific plev and iterates over each latitude up to the equator
# opposite ends of lat. values for Ozone 
import xarray as xr
import numpy as np
import os
import matplotlib.pyplot as plt

# Input and output file names
in_file = "cmip6_radozone_picontrol_1850_monthly_128_64.999.nc"
out_file = "avgOzoneCalc_TIME_Results2.nc"
# Open input file to work with data inside of it
data = xr.open_dataset(in_file)
# Create a copy for data
data_copy = data.copy()

# OZ(Ozone) is a float (with a negative exponential)
OZ_data = data['OZ']
# Create a copy of OZ_data so as to not modify the original
# This is a seperate copy from data_copy as it is meant to work with
OZ_data_copy = OZ_data.copy()
#(tim)e first first, Pressure Level (plev) second, (lat)itude third, (lon)gtitude last in array

month_day_weights = [31, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31, 31]
#weights = np.array(month_day_weights) / np.sum(month_day_weights)

##########
# Dec. --> Jan. Mar. --> Apr. May --> Jun. Jul. --> Aug. --> Sep. Oct. --> Nov. == 31 Dec. --> Jan  (0, 3, 5, 7, 8, 10, 12)
# Jan. --> Feb. Apr. --> May Jun. --> Jul. Sep. --> Oct. Nov. --> Dec. == 30 (1, 4, 6, 9, 11)
# Feb. --> Mar. == 28 (2)
##########
# Function:
# (X1*W1 + X2*W2 + X3*W3 + X4*W4 + X5*W5 + X6*W6 + X7*W7 + X8*W8 + X9*W9 + X10*W10 + X11*W11 + X12*W12)
# -------------------------------------------------------------------------------------------------------
#               (W1 + W2 + W3 + W4 + W5 + W6 + W7 + W8 + W9 + W10 + W11 + W12)

# This loop goes through all pressure index values
for plev_index in range(data_copy.dims['plev']):
    # Subset of 1 defined index (OZ[:, defined_plev_index, :, :])
    # ":" Represents for all possible values
    # Purpose of creating a subset is to be able to work within a specific index without needing to
    # explicitly define the index of, for example, plev (Pressure Level) each subsequent time it is used
    subset_pressure = data_copy.isel(plev=plev_index)
    # Loop through lat. values to equator
    for lat_index_bot in range(32):
        lat_index_top = 63 - lat_index_bot
        
        OZ_weighted_time_avg_calc = 0
        
        for time_index in range(data_copy.dims['time']):
            #OZ_weighted_time_avg_calc += OZ_data_copy[time_index, plev_index, :, :] * month_day_weights[time_index]
            OZ_weighted_time_avg_calc += subset_pressure['OZ'].isel(time = time_index) * month_day_weights[time_index]
        
        OZ_weighted_time_avg_calc_result = OZ_weighted_time_avg_calc/(np.sum(month_day_weights)) # x/427

        #OZ_data_copy[:, plev_index, :, :] = OZ_weighted_time_avg_calc_result
        OZ_data_copy[:, plev_index, :, :] = OZ_weighted_time_avg_calc_result

        #OZ_weighted_time_avg_calc = (OZ_data_copy * weights).sum(dim='time')
        #OZ_time_avg_calc = subset_pressure.mean(dim='time')
        

        #weights_month = xr.DataArray(month_day_weights, dims='time', coords={'time': subset_pressure.time})
        
        '''
        OZ_data_copy['OZ'](weights_month)
        weighted_mean = OZ_data_copy.mean(("time"))

        #average_value = (subset_pressure * weights_month).sum(dim='time') / np.sum(month_day_weights)
        #OZ_data_updated = subset_pressure.loc[dict(plev=plev_index)] = average_value
        '''     
        # This uses the 2 indexes to extract the value of Ozone (subset_time['OZ'].isel(lat = X)) at value X
        OZ_lat_avg_calc = (OZ_data_copy.isel(lat = lat_index_bot) + OZ_data_copy.isel(lat = lat_index_top))/2
        # This section adds the avg. value calculated above into the specific index of the Ozone data
        OZ_data_copy[:, plev_index, lat_index_bot, :] = OZ_lat_avg_calc
        OZ_data_copy[:, plev_index, lat_index_top, :] = OZ_lat_avg_calc

# Write results to file
OZ_data_copy.to_netcdf(out_file, 'w')
dataOut = xr.open_dataset(out_file)
print("\nFile named " + out_file + " succesfully written to directory:\n" + os.path.abspath(out_file) + "\n")

# Subset of the original data to generate a plot
subset_origin = OZ_data.isel(time = 0, lon = 21)
subset_origin_values = subset_origin.values
image_out_name = "avg_ozone_time_plot_CONTROL.png"
# Parameters for graph
plt.figure(figsize=(8, 6))
plt.imshow(subset_origin_values, cmap='jet', vmin=subset_origin_values.min(), vmax=subset_origin_values.max())
plt.colorbar(label='OZ values')
plt.title(f'Ozone Data: Time = 0, Pressure Level = 20, Lat = 0, Lon = 0')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.savefig(image_out_name)
print(image_out_name + " generated")

# Subset of the modified data to generate a plot
subset_copy = OZ_data_copy.isel(time = 0, lon = 0)
subset_copy_values = subset_copy.values
mod_image_out_name = "avg_ozone_time_plot_CALCULATED.png"
# Parameters for graph
plt.figure(figsize=(8, 6))
plt.imshow(subset_copy_values, cmap='jet', vmin=subset_copy_values.min(), vmax=subset_copy_values.max())
plt.colorbar(label='Modified OZ values')
plt.title(f'Ozone Data: Time = 0, Pressure Level = 20, Lat = 0, Lon = 0')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.savefig(mod_image_out_name)
print(mod_image_out_name + " generated\n")