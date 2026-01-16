from math import pi

AVAILABLE_ANGLE_UNITS = ['degree', 'rad']

def compute_cl(alpha, alpha_L0=0.0, **kwargs):
    units = kwargs.get('units', 'degree')
    if units not in AVAILABLE_ANGLE_UNITS:
        raise RuntimeError(f"Expected units to be in {AVAILABLE_ANGLE_UNITS}, got {units}.")
    if units == 'degree':
        alpha*=pi/180.0
        alpha_L0*=pi/180.0
    return 2.0*pi*(alpha-alpha_L0)

def compute_cd(alpha, alpha_L0=0.0, **kwargs):
    return 0.0
