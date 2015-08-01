
def calc_bmi(weight, height, hunit='m'):
    if hunit == 'cm':
        height /= 100.0
    return float(weight)/height**2


print calc_bmi(50, 150, 'cm')

print calc_bmi(weight=50, height=1.7)

print calc_bmi(height=1.7, weight=50)

print calc_bmi(height=170, weight=50, hunit='cm')

print calc_bmi(height=170, weight=50, hunit='cm')
