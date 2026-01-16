def parse_kwargs(items):
    """
    Convert a list of strings like ["key=value", "foo=3.14"]
    into a dictionary suitable for **kwargs.
    """
    kwargs = {}
    for item in items:
        if "=" not in item:
            raise ValueError(f"Invalid argument '{item}', expected key=value")
        key, value = item.split("=", 1)

        # very basic type inference
        if value.isdigit():
            value = int(value)
        else:
            try:
                value = float(value)
            except ValueError:
                pass  # keep as string

        kwargs[key] = value
    return kwargs
