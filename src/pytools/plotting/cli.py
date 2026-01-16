from pathlib import Path
from pytools.plotting.plot import plot
from pytools.cli_utils import parse_kwargs

def register(subparsers):
    parser = subparsers.add_parser(
        "plot",
        help="Plot data files",
        description="Plot data files using matplotlib"
    )

    parser.add_argument(
        "file",
        help="Input data file"
    )

    parser.add_argument(
        "kwargs",
        nargs="*",
        metavar="key=value",
        help="Forwarded keyword arguments (e.g. skiprows=1)"
    )

    parser.set_defaults(func=run)

def run(args):
    fname = Path(args.file).resolve()
    kwargs = parse_kwargs(args.kwargs)
    plot(fname, **kwargs)
