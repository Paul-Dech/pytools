import argparse

def main():
    parser = argparse.ArgumentParser(
        prog="pytools",
        description="Personal Python scientific toolbox"
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=True,
        title="commands"
    )

    from pytools.plotting.cli import register as plot_register
    from pytools.calc.cli import register as calc_register

    plot_register(subparsers)
    calc_register(subparsers)

    args = parser.parse_args()
    args.func(args)
