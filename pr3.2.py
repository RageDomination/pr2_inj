import numpy as np
from scipy.stats import chi2, t

# Дані
data = np.array([
    [0.41, 510, 2140, 218.52, 8941.9, 10.2233, 3.31818],
    [0.33, 400, 1270, 226.99, 5359.4, 5.26866, 4.45454],
    [0.74, 630, 2670, 440.44, 8769.9, 4.67550, 2.15151],
    [0.57, 490, 810, 159.23, 5703.3, 3.38450, 2.92424],
    [0.67, 460, 3060, 181.25, 4155.7, 4.53593, 1.98484]
])

m, n = data.shape  # m — експерти, n — фактори

# 1. Перетворення у ранги
ranks = np.zeros_like(data)

for i in range(m):
    order = data[i].argsort()
    ranks[i][order] = np.arange(1, n + 1)

print("Матриця рангів:\n", ranks)

# 2. Суми рангів
R = np.sum(ranks, axis=0)
print("\nСуми рангів:", R)

# 3. Коефіцієнт Кендалла
R_mean = np.mean(R)
S = np.sum((R - R_mean) ** 2)

W = 12 * S / (m**2 * (n**3 - n))
print(f"\nКоефіцієнт конкордації W = {W:.4f}")

# 4. Критерій Пірсона
chi_square = m * (n - 1) * W
df = n - 1
chi_critical = chi2.ppf(0.95, df)

print(f"\nχ² = {chi_square:.4f}")
print(f"χ² критичне = {chi_critical:.4f}")

# 5. Критерій Ст’юдента
if W == 1:
    t_value = float('inf')
else:
    t_value = W * np.sqrt((m * (n - 1)) / (1 - W))

t_critical = t.ppf(0.975, df)

print(f"\nt = {t_value:.4f}")
print(f"t критичне = {t_critical:.4f}")

# 6. Висновок
print("\nВисновок:")

if chi_square > chi_critical:
    print("Узгодженість за Пірсоном є значущою")
else:
    print("Узгодженість за Пірсоном НЕ значуща")

if t_value > t_critical:
    print("Узгодженість підтверджена за критерієм Ст’юдента")
else:
    print("Узгодженість НЕ підтверджена за Ст’юдентом")