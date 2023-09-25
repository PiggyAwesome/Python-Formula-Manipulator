from sympy import symbols, solve, Eq, Equality, latex, pprint, init_printing
init_printing(use_latex=True) 


mass = symbols("m")
time = symbols("t")
acceleration = symbols("a")
force = symbols("F")
time = symbols("t")
work = symbols("W")
displacement = symbols("s")
power = symbols("P")
angle_of_force_to_direction_of_movement = symbols("θ")

"""
F = ma

W = Fscos(θ)

P = W/∆t
"""

formulas:list[Equality] = [
    Eq(force, mass*acceleration),
    Eq(work, force*displacement),
    Eq(power, work/time),
]


variables = {  
    "F": force,
    "a": acceleration,
    "m": mass,
    "W": work,
    "s": displacement,
    "t": time,
    "P": power,
    "θ": angle_of_force_to_direction_of_movement
}

print("""
      (F) Force
      (a) Acceleration
      (m) Mass
      (W) Work
      (s) Displacement
      (t) Time
      (P) Power
      (θ) Angle of force to direction of movement

...
""")

requested = input("What variable do you need?\n:: ")

requested_object = variables.get(requested)

possible_formulae = []
for formula in formulas:
    has_var = bool(formula.find(requested_object))
    if has_var: possible_formulae.append(formula)


for formula in possible_formulae:
    required_variables:set = formula.free_symbols
    required_variables.remove(requested_object)

    for variable in required_variables:
        has_variable = input(f"Do you have the value of ({variable})? (y/n): ")
        if has_variable != "y": print("Checking next formula..."); break

    else:

        print(f"Your formula is the following:")
        pprint(solve(formula, requested_object)[0], use_unicode=True)
        break

