import numpy as np
import pylab
from matplotlib import pyplot as plt

# dist_path = 'position_osc.txt'
#
# time_list = []
# dist_list = []
#
# dist_file = open(dist_path, "r")
# i = 0
# for line in dist_file:
#     if i > 1:
#         time_list.append(float(line[:5]))
#         dist_list.append(float(line[6:12]))
#     i += 1


# fig, ax = plt.subplots()
# ax.plot(time_list, dist_list)
#
# ax.set(xlabel='Time (s)', ylabel='Distance (cm)',
#        title='Distance vs. Time')
# ax.grid()
#
# fig.savefig("test.png")
# # plt.show()


# WITH DAMPING

m = 0.2
k = 16.63
time_generated = []
distance_generated = []
velocity_generated = []
delta_t_too_big = 0.01
delta_t = 0.01
curr_time = 0
y_1 = 2.0985
v_1 = 3.2078
period = 10.0
omega_0 = 9.1193
energy_generated = []
E = 0
coef_damping = 0.1



def damped_system_distance_vs_time():
    m = 0.2
    k = 16.63
    time_generated = []
    distance_generated = []
    velocity_generated = []
    delta_t_too_big = 0.01
    delta_t = 0.01
    curr_time = 0
    y_1 = 2.0985
    v_1 = 3.2078
    period = 10.0
    omega_0 = 9.1193
    energy_generated = []
    E = 0
    coef_damping = 0.1
    curr_time = 0

    while curr_time < 10:
        time_generated.append(curr_time)
        distance_generated.append(y_1)
        velocity_generated.append(v_1)
        v_1 = v_1 + delta_t * (-1 * (omega_0 ** 2) * y_1 - coef_damping * v_1)
        y_1 = y_1 + delta_t * v_1
        E = (m * v_1 * v_1 + k * y_1 * y_1) / 2
        energy_generated.append(E)
        curr_time += delta_t

    fig, ax = plt.subplots()
    ax.plot(time_generated, distance_generated)
    # ax.plot(time_generated, velocity_generated)
    # ax.plot(distance_generated, velocity_generated)

    # ax.plot(distance_generated, energy_generated)
    # ax.plot(time_generated, energy_generated)
    ax.set(xlabel='Time (s)', ylabel='Distance (cm)',
           title='Distance vs. Time')
    ax.grid()

    fig.savefig("DistanceVsTime_Damped.png")

    plt.show()

def damped_system_velocity_vs_time():
    m = 0.2
    k = 16.63
    time_generated = []
    distance_generated = []
    velocity_generated = []
    delta_t_too_big = 0.01
    delta_t = 0.01
    curr_time = 0
    y_1 = 2.0985
    v_1 = 3.2078
    period = 10.0
    omega_0 = 9.1193
    energy_generated = []
    E = 0
    coef_damping = 0.1
    curr_time = 0

    while curr_time < 10:
        time_generated.append(curr_time)
        distance_generated.append(y_1)
        velocity_generated.append(v_1)
        v_1 = v_1 + delta_t * (-1 * (omega_0 ** 2) * y_1 - coef_damping * v_1)
        y_1 = y_1 + delta_t * v_1
        E = (m * v_1 * v_1 + k * y_1 * y_1) / 2
        energy_generated.append(E)
        curr_time += delta_t

    fig, ax = plt.subplots()
    ax.plot(time_generated, velocity_generated)
    # ax.plot(time_generated, velocity_generated)
    # ax.plot(distance_generated, velocity_generated)

    # ax.plot(distance_generated, energy_generated)
    # ax.plot(time_generated, energy_generated)
    ax.set(xlabel='Time (s)', ylabel='Velocity (cm)',
           title='Velocity vs. Time')
    ax.grid()

    fig.savefig("VelocityVsTime_Damped.png")

    plt.show()

def damped_system_energy_vs_time():
    m = 0.2
    k = 16.63
    time_generated = []
    distance_generated = []
    velocity_generated = []
    delta_t_too_big = 0.01
    delta_t = 0.01
    curr_time = 0
    y_1 = 2.0985
    v_1 = 3.2078
    period = 10.0
    omega_0 = 9.1193
    energy_generated = []
    E = 0
    coef_damping = 0.1
    curr_time = 0

    while curr_time < 10:
        time_generated.append(curr_time)
        distance_generated.append(y_1)
        velocity_generated.append(v_1)
        v_1 = v_1 + delta_t * (-1 * (omega_0 ** 2) * y_1 - coef_damping * v_1)
        y_1 = y_1 + delta_t * v_1
        E = (m * v_1 * v_1 + k * y_1 * y_1) / 2
        energy_generated.append(E)
        curr_time += delta_t

    fig, ax = plt.subplots()
    ax.plot(time_generated, energy_generated)
    # ax.plot(time_generated, velocity_generated)
    # ax.plot(distance_generated, velocity_generated)

    # ax.plot(distance_generated, energy_generated)
    # ax.plot(time_generated, energy_generated)
    ax.set(xlabel='Time (s)', ylabel='Energy (J)',
           title='Energy vs. Time')
    ax.grid()

    fig.savefig("EnergyVsTime_Damped.png")

    plt.show()


# print(time_generated)
# print(distance_generated)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    damped_system_energy_vs_time()

