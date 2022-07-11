#carpet area
floor = [10, 10]

#wall area
face1 = [10, 5]
face2 = [10, 5]
face3 = [10, 5]
face4 = [10, 5]

#window area and numbers
w_area = 2
n_face1 = 4
n_face2 = 4
n_face3 = 4
n_face4 = 4

#temperature
t_ext = 20
t_int = -16

ow = face1[0]*face1[1]+face2[0]*face2[1]+face3[0]*face3[1]+face4[0]*face4[1]      #outer wall area
wi = (n_face1+n_face2+n_face3+n_face4)*w_area                                     #window area total
bc = floor[0]*floor[1]                                                            #basement ceiling
tsc = floor[0]*floor[1]                                                           #top storey ceiling

net_area = (ow-wi)+wi+bc+tsc
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

t_ow = transmission((ow-wi),1, 0.28, 0.1)
t_wi = transmission(wi, 1, 1.3, 0.1)
t_bc = transmission(bc, 0.4, 0.35, 0.1)
t_tsc = transmission(tsc, 0.4, 0.20, 0.1)
t = t_ow + t_wi + t_bc + t_tsc
v = ventilation(0.5, 3, 0.03, 1)
h = heat_up_load(ow, 21)
Heat_Load = t+v+h
Specific_heat_load = Heat_Load/ow
print("Transmission heat: ", t)
print("Ventilation heat: ", v)
print("Heat-up Load: ", h)
print("Heat Load: ", Heat_Load)
print("Specific Heat Load: ", Specific_heat_load)

