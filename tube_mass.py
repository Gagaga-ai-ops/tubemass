import math


def circle_area(d):
    """Площадь круга с диаметром d."""
    return math.pi * d ** 2 / 4


def tube_cross_section(d_out, d_in):
    """Площадь поперечного сечения трубы."""
    return circle_area(d_out) - circle_area(d_in)


def tube_mass(d_out, d_in, length, density=7850):
    """Масса трубы в кг (размеры в метрах, плотность в кг/м³)."""
    return tube_cross_section(d_out, d_in) * length * density


print(tube_mass(0.060, 0.050, 6))                 # ocelová trubka: ≈ 40.69 kg
print(tube_mass(0.060, 0.050, 6, density=2700))   # hliníková: ≈ 14.00 kg

# Расширение: таблица масс 6-метровых стальных труб, D = 60 мм, стенка 1..5 мм
print()
print("Стенка, мм | Масса, кг")
print("-----------+----------")
D_OUT = 0.060
for wall_mm in range(1, 6):
    d_in = D_OUT - 2 * wall_mm / 1000
    print(f"{wall_mm:>10} | {tube_mass(D_OUT, d_in, 6):>8.2f}")
