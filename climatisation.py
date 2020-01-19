import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

temperature = ctrl.Antecedent(np.arange(5, 65, 1), 'temperature')
humidity = ctrl.Antecedent(np.arange(16, 100, 1), 'humidity')
power = ctrl.Consequent(np.arange(0, 3, 0.001), 'power')

temperature['VVC'] = fuzz.trimf(temperature.universe, [5, 5, 15])
temperature['VC'] = fuzz.trimf(temperature.universe, [5, 15, 25])
temperature['C'] = fuzz.trimf(temperature.universe, [15, 25, 35])
temperature['F'] = fuzz.trimf(temperature.universe, [25, 35, 45])
temperature['H'] = fuzz.trimf(temperature.universe, [35, 45, 55])
temperature['VH'] = fuzz.trimf(temperature.universe, [45, 55, 65])
temperature['VVH'] = fuzz.trimf(temperature.universe, [55, 65, 65])


humidity['VVL'] = fuzz.trimf(humidity.universe, [16, 16, 30])
humidity['VL'] = fuzz.trimf(humidity.universe, [16, 30, 44])
humidity['L'] = fuzz.trimf(humidity.universe, [30, 44, 58])
humidity['M'] = fuzz.trimf(humidity.universe, [44, 58, 72])
humidity['H'] = fuzz.trimf(humidity.universe, [58, 72, 86])
humidity['VH'] = fuzz.trimf(humidity.universe, [72, 86, 100])
humidity['VVH'] = fuzz.trimf(humidity.universe, [86, 100, 100])


power['VVL'] = fuzz.trapmf(power.universe, [0, 0, 0.166, 0.333])
power['VL'] = fuzz.trapmf(power.universe, [0.166, 0.333, 0.666, 0.833])
power['L'] = fuzz.trapmf(power.universe, [0.666, 0.833, 1.166, 1.333])
power['M'] = fuzz.trapmf(power.universe, [1.166, 1.333, 1.666, 1.833])
power['H'] = fuzz.trapmf(power.universe, [1.666, 1.833, 2.166, 2.333])
power['VH'] = fuzz.trapmf(power.universe, [2.166, 2.333, 2.666, 2.833])
power['VVH'] = fuzz.trapmf(power.universe, [2.666, 2.833, 3, 3])


ruleVVL1 = ctrl.Rule(temperature['VVC'] | humidity['VVL'], power['VVL'])
ruleVVL2 = ctrl.Rule(temperature['VVC'] | humidity['VL'], power['VVL'])
ruleVVL3 = ctrl.Rule(temperature['VC'] | humidity['VVL'], power['VVL'])
ruleVL1 = ctrl.Rule(temperature['C'] | humidity['VVL'], power['VL'])
ruleVL2 = ctrl.Rule(temperature['F'] | humidity['VVL'], power['VL'])
ruleVL3 = ctrl.Rule(temperature['VC'] | humidity['VL'], power['VL'])
ruleVL4 = ctrl.Rule(temperature['C'] | humidity['VL'], power['VL'])
ruleVL5 = ctrl.Rule(temperature['VVC'] | humidity['L'], power['VL'])
ruleVL6 = ctrl.Rule(temperature['VC'] | humidity['L'], power['VL'])
ruleVL7 = ctrl.Rule(temperature['VVC'] | humidity['M'], power['VL'])
ruleL1 = ctrl.Rule(temperature['F'] | humidity['VL'], power['L'])
ruleL2 = ctrl.Rule(temperature['C'] | humidity['L'], power['L'])
ruleL3 = ctrl.Rule(temperature['F'] | humidity['L'], power['L'])
ruleL4 = ctrl.Rule(temperature['VC'] | humidity['M'], power['L'])
ruleL5 = ctrl.Rule(temperature['C'] | humidity['M'], power['L'])
ruleM1 = ctrl.Rule(temperature['VVH'] | humidity['VVL'], power['M'])
ruleM2 = ctrl.Rule(temperature['VH'] | humidity['VL'], power['M'])
ruleM3 = ctrl.Rule(temperature['H'] | humidity['L'], power['M'])
ruleM4 = ctrl.Rule(temperature['F'] | humidity['M'], power['M'])
ruleM5 = ctrl.Rule(temperature['C'] | humidity['H'], power['M'])
ruleM6 = ctrl.Rule(temperature['VC'] | humidity['VH'], power['M'])
ruleM7 = ctrl.Rule(temperature['VVC'] | humidity['VVH'], power['M'])
ruleH1 = ctrl.Rule(temperature['VVH'] | humidity['VL'], power['H'])
ruleH2 = ctrl.Rule(temperature['VH'] | humidity['L'], power['H'])
ruleH3 = ctrl.Rule(temperature['VVH'] | humidity['L'], power['H'])
ruleH4 = ctrl.Rule(temperature['H'] | humidity['M'], power['H'])
ruleH5 = ctrl.Rule(temperature['VH'] | humidity['M'], power['H'])
ruleH6 = ctrl.Rule(temperature['F'] | humidity['H'], power['H'])
ruleH7 = ctrl.Rule(temperature['H'] | humidity['H'], power['H'])
ruleH8 = ctrl.Rule(temperature['C'] | humidity['VH'], power['H'])
ruleH9 = ctrl.Rule(temperature['F'] | humidity['VH'], power['H'])
ruleH10 = ctrl.Rule(temperature['VC'] | humidity['VVH'], power['H'])
ruleH11 = ctrl.Rule(temperature['C'] | humidity['VVH'], power['H'])
ruleVH1 = ctrl.Rule(temperature['VVH'] | humidity['M'], power['VH'])
ruleVH2 = ctrl.Rule(temperature['VH'] | humidity['H'], power['VH'])
ruleVH3 = ctrl.Rule(temperature['VVH'] | humidity['H'], power['VH'])
ruleVH4 = ctrl.Rule(temperature['H'] | humidity['VH'], power['VH'])
ruleVH5 = ctrl.Rule(temperature['VH'] | humidity['VH'], power['VH'])
ruleVH6 = ctrl.Rule(temperature['F'] | humidity['VVH'], power['VH'])
ruleVH7 = ctrl.Rule(temperature['H'] | humidity['VVH'], power['VH'])
ruleVVH1 = ctrl.Rule(temperature['VVH'] | humidity['VH'], power['VVH'])
ruleVVH2 = ctrl.Rule(temperature['VH'] | humidity['VVH'], power['VVH'])
ruleVVH3 = ctrl.Rule(temperature['VVH'] | humidity['VVH'], power['VVH'])




power_ctrl = ctrl.ControlSystem([ruleL1, ruleL2, ruleL3, ruleL4, ruleL5, ruleM1, ruleVL1, ruleVL2, ruleVL3, ruleVL4,
                                 ruleVL5, ruleVL6, ruleVL7, ruleVVL1, ruleVVL2, ruleVVL3, ruleM2, ruleM3, ruleM4,
                                 ruleM5, ruleM6, ruleM7, ruleH1, ruleH2, ruleH3, ruleH4, ruleH5, ruleH6, ruleH7,
                                 ruleH8, ruleH9, ruleH10, ruleH11, ruleVH1, ruleVH2, ruleVH3, ruleVH4, ruleVH5,
                                 ruleVH6, ruleVH7, ruleVVH1, ruleVVH2, ruleVVH3])
power_check = ctrl.ControlSystemSimulation(power_ctrl)

power_check.input['temperature'] = 40
power_check.input['humidity'] = 37

power_check.compute()

print(power_check.output['power'])
#power.view(sim=power_check)



