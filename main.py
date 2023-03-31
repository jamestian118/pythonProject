import matplotlib.pyplot as plt
import numpy as np
import sympy

# 定义符号变量
t = sympy.Symbol('t')

# 定义一个分段函数
def f1(t):
    return sympy.Piecewise((5 + 0*t + 15/2*t**2 - 5/2*t**3, t < 2),
                           (15 - 0*(t-2) + 75/4*(t-2)**2 - 25/4*(t-2)**3, t >= 2))

# 生成 t 的取值范围
t_values = np.linspace(0, 4, 1000)

# 绘制函数图像和导数图像
plt.plot(t_values, [f1(t_val).evalf() for t_val in t_values], label='θ(t)')
plt.plot(t_values, [sympy.diff(f1(t), t).subs(t, x).evalf() for x in t_values], label='dθ/dt')
plt.plot(t_values, [sympy.diff(f1(t), t, 2).subs(t, x).evalf() for x in t_values], label='d²θ/dt²')

# 添加图例和坐标轴标签
plt.legend()
plt.xlabel('t')
plt.ylabel('θ(t)')

# 显示图像
plt.show()
