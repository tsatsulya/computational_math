from lsm import least_square_method

import numpy as np
import matplotlib.pyplot as plt
import math

population = [ 144444359, 144713314, 145102755, 145617329, 145742286, 145652293, 145452536, 
145109157, 144668389, 144285070, 143956866, 143629362, 143364543, 143242599, 
143163643, 143086549, 143117693, 143338669, 143800049, 144353636, 144946723, 
145590136, 146235530, 146844839 ]

years = list(range(2000, 2024))

print(least_square_method(years, population))

plt.figure(figsize=(16/2, 9/2))
plt.title(r'$Root\:of\:the\:equation$')
plt.grid(linestyle='--', linewidth=0.5)
plt.xlabel(r'$iteration\:number$')
plt.ylabel(r'$root\:value$')
plt.tight_layout()
plt.plot(years, population, 'o')

plt.savefig('img/population.jpg', dpi=500)