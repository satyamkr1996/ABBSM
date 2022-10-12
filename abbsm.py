# -*- coding: utf-8 -*-
"""ABBSM.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17MRXvmfmqxltE5bSvU-s4HDETTCYpQWy
"""

import pandas as pd
file = pd.read_csv("ABBSM_Data.csv")
#House Type Selection
print("Select House Type from the following options: ")
for i in range(50):
    print(str(i+1) + "." + " " + file.House_Type[i])
House_type = input("Your Selection: ")

#Data Reading from file
for i in range(50):
  if House_type == file.House_Type[i]:
    #Area
    Roof_1_area = file.Roof_1_A[i]
    Roof_2_area = file.Roof_2_A[i]
    Wall_1_area = file.Wall_1_A[i]
    Wall_2_area = file.Wall_2_A[i]
    Wall_3_area = file.Wall_3_A[i]
    Floor_1_area = file.Floor_1_A[i]
    Floor_2_area = file.Floor_2_A[i]
    Window_1_area = file.Window_1_A[i]
    Window_2_area =file.Window_2_A[i]
    Door_1_area = file.Door_1_A[i]

    #U-value
    Roof_1_uvalue = file.Roof_1_UW[i]
    Roof_2_uvalue = file.Roof_2_UW[i]
    Wall_1_uvalue = file.Wall_1_UW[i]
    Wall_2_uvalue = file.Wall_2_UW[i]
    Wall_3_uvalue = file.Wall_3_UW[i]
    Floor_1_uvalue = file.Floor_1_UW[i]
    Floor_2_uvalue = file.Floor_2_UW[i]
    Window_1_uvalue = file.Window_1_UW[i]
    Window_2_uvalue =file.Window_2_UW[i]
    Door_1_uvalue = file.Door_1_UW[i]


#temperature
t_ext = 20
t_int = -16

Wall_Area = Wall_1_area + Wall_2_area + Wall_3_area      #outer wall area
Window_Area = Window_1_area + Window_2_area              #window area total
Roof_Area = Roof_1_area + Roof_2_area                    #roof area total
Floor_Area = Floor_1_area + Floor_2_area                 #floor area total

net_area = (Wall_Area - Window_Area) + Window_Area + Roof_Area + Floor_Area
gross_vol = floor[0]*floor[1]*face1[1]
net_vol = 0.8*gross_vol

def transmission(area, correction_factor, u_value, heat_bridge):
    u_corrected = u_value+heat_bridge
    ht = area*correction_factor*u_corrected
    t_heat_loss = ht*(t_ext-t_int)
    return t_heat_loss

def ventilation(n_min, n50, e, eps):
    v_min = n_min*net_vol
    v_inf = 2*net_vol*n50*e*eps
    vi = max(v_min, v_inf)
    v_heat_loss = 0.34*vi*(t_ext - t_int)
    return v_heat_loss

def heat_up_load(frh, area):
    heatupload = area*frh
    return heatupload

t_wall = transmission(Wall_1_area,1, Wall_1_uvalue, 0.1) + transmission(Wall_2_area,1, Wall_2_uvalue, 0.1) + transmission(Wall_3_area,1, Wall_3_uvalue, 0.1)
t_window = transmission(Window_1_area, 1, Window_1_uvalue, 0.1) + transmission(Window_2_area,1, Window_2_uvalue, 0.1)
t_roof = transmission(Roof_1_area, 0.4, Roof_1_uvalue, 0.1) + transmission(Roof_2_area,1, Roof_2_uvalue, 0.1)
t_floor = transmission(Floor_1_area, 0.4, Floor_1_uvalue, 0.1) + transmission(Floor_2_area,1, Floor_2_uvalue, 0.1)
total_transmission = t_wall + t_window + t_roof + t_floor
total_ventilation = ventilation(0.5, 3, 0.03, 1)
total_heat_up_load = heat_up_load(21, Wall_1_area) + heat_up_load(21, Wall_2_area) + heat_up_load(21, Wall_3_area)
Heat_Load = total_transmission + total_ventilation + total_heat_up_load
Specific_heat_load = Heat_Load/(Wall_1_area + Wall_2_area + Wall_3_area)
print("Transmission heat: ", total_transmission)
print("Ventilation heat: ", total_ventilation)
print("Heat-up Load: ", total_heat_up_load)
print("Heat Load: ", Heat_Load)
print("Specific Heat Load: ", Specific_heat_load)