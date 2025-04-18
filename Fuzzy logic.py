import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# تعريف (درجة الحرارة) المدخلات و(مستوى التدفئة) المخرجات
temperature = ctrl.Antecedent(np.arange(0, 41, 1), 'temperature')
heating = ctrl.Consequent(np.arange(0, 101, 1), 'heating')

# تعريف الدوال العضوية
temperature['cold'] = fuzz.trimf(temperature.universe, [0, 0, 20])
temperature['comfortable'] = fuzz.trimf(temperature.universe, [15, 22, 28])
temperature['hot'] = fuzz.trimf(temperature.universe, [25, 40, 40])

heating['low'] = fuzz.trimf(heating.universe, [0, 0, 50])
heating['medium'] = fuzz.trimf(heating.universe, [25, 50, 75])
heating['high'] = fuzz.trimf(heating.universe, [50, 100, 100])

# إنشاء القواعد الضبابية
rule1 = ctrl.Rule(temperature['cold'], heating['high'])
rule2 = ctrl.Rule(temperature['comfortable'], heating['medium'])
rule3 = ctrl.Rule(temperature['hot'], heating['low'])

# بناء نظام التحكم الضبابي
heating_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
heating_simulation = ctrl.ControlSystemSimulation(heating_ctrl)

# الإدخال من المستخدم مع التحقق من صحة المدخلات
try:
    temperature_input = float(input('ادخل درجة حرارة الغرفة (C): '))
    if temperature_input < 0 or temperature_input > 40:
        raise ValueError("يجب أن تكون درجة الحرارة بين 0 و 40 درجة مئوية.")
except ValueError as e:
    print(f'خطأ: {e}')
else:
    # إدخال الدرجة في النظام
    heating_simulation.input['temperature'] = temperature_input

    # حساب النتائج
    heating_simulation.compute()

    # عرض النتيجة
    heating_output = heating_simulation.output['heating']
    print(f'مستوى التدفئة المطلوبة: {heating_output:.2f}%')

    # إعداد الرسم البياني
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))

    # رسم دوال درجة الحرارة
    temperature.view(sim=heating_simulation)
    plt.title('دوال درجة الحرارة')
    plt.xlabel('درجة الحرارة (C)')
    plt.ylabel('العضوية')

    # رسم دوال مستوى التدفئة
    heating.view(sim=heating_simulation)
    plt.title('دوال مستوى التدفئة')
    plt.xlabel('مستوى التدفئة (%)')
    plt.ylabel('العضوية')

    # عرض المخططات
    plt.tight_layout()
    plt.show()
