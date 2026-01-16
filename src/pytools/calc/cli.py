from pathlib import Path
from pytools.calc.thin_airfoil.aero_coeffs import compute_cl, compute_cd
from pytools.cli_utils import parse_kwargs

def register(subparsers):
    parser = subparsers.add_parser(
        "calc",
        help="Quick computation",
        description="Perform quick evaluation of the lift and drag coefficients using thin airfoil theory"
    )

    parser.add_argument(
        "alpha",
        type=float,
        help="angle of attack"
    )
    parser.add_argument(
        "alpha_L0",
        nargs="?", # optional
        type=float,
        default=0.0, # default value if not given
        help="Angle of attack (deg), default=0.0"
    )

    parser.add_argument(
        "kwargs",
        nargs="*",
        metavar="key=value",
        help="Forwarded keyword arguments (e.g. units='degree')"
    )

    parser.set_defaults(func=run)

def run(args):
    alpha = getattr(args, "alpha", 0.0)  # numeric
    alpha_L0 = getattr(args, "alpha_L0", 0.0)
    kwargs = parse_kwargs(getattr(args, "kwargs", []))

    units = kwargs.get('units', 'degree')
    print(f'Thin airfoil theory for aoa {alpha} {units}.')
    print('cl', compute_cl(alpha, alpha_L0, **kwargs))
    print('cd', compute_cd(alpha, alpha_L0, **kwargs))
