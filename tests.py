
def test_base():
    from pylama_pylint import Linter
    assert Linter


def test_pylint():
    from pylama.core import run
    from pylama.config import parse_options

    options = parse_options(linters=['pylint'], config=False)
    options.ignore = set(['R0912', 'C0111'])
    errors = run('pylama_pylint/pylint/utils.py', options=options)
    assert len(errors) == 23
    assert errors[0].number == 'W0622'

    options.linters_params['pylint'] = dict(disable="W")
    errors = run('pylama_pylint/pylint/utils.py', options=options)
    assert len(errors) == 19
    assert errors[0].number == 'C0330'

    options.linters_params['pylint']['max_line_length'] = 200
    errors = run('pylama_pylint/pylint/utils.py', options=options)
    assert len(errors) == 3


# pylama:ignore=D
