from sympy import Symbol, log, sqrt, sin, S
from sympy.plotting.textplot import textplot_str


def test_axes_alignment():
    x = Symbol('x')
    lines = [
        "      1 |                                                      ..",
        "        |                                                   ...  ",
        "        |                                                ...     ",
        "        |                                            ....        ",
        "        |                                         ...            ",
        "        |                                      ...               ",
        "        |                                   ...                  ",
        "        |                                ...                     ",
        "0.05882 | ----------------------------...------------------------",
        "        |                         ....                           ",
        "        |                      ...                               ",
        "        |                   ...                                  ",
        "        |                ...                                     ",
        "        |             ...                                        ",
        "        |         ....                                           ",
        "        |      ...                                               ",
        "        |   ...                                                  ",
        "     -1 | ..                                                     ",
        "          -1                         0                          1"
    ]
    assert lines == list(textplot_str(x, -1, 1))

    lines = [
        '      1 |                                                      ..',
        '        |                                                  ....  ',
        '        |                                               ...      ',
        '        |                                            ...         ',
        '        |                                        ....            ',
        '        |                                     ...                ',
        '        |                                  ...                   ',
        '        |                              ....                      ',
        '      0 | --------------------------...--------------------------',
        '        |                       ....                             ',
        '        |                    ...                                 ',
        '        |                 ...                                    ',
        '        |             ....                                       ',
        '        |          ...                                           ',
        '        |       ...                                              ',
        '        |   ....                                                 ',
        '     -1 | ..                                                     ',
        '          -1                         0                          1'
    ]
    assert lines == list(textplot_str(x, -1, 1, H=17))


def test_singularity():
    x = Symbol('x')
    lines = [
        '     54 |  .                                                     ',
        '        |                                                        ',
        '        |                                                        ',
        '        |                                                        ',
        '        |                                                        ',
        '        |                                                        ',
        '        |                                                        ',
        '        |                                                        ',
        '29.0588 | -------------------------------------------------------',
        '        |   .                                                    ',
        '        |                                                        ',
        '        |                                                        ',
        '        |    .                                                   ',
        '        |     \\                                                  ',
        '        |      ..                                                ',
        '        |        ...                                             ',
        '        |           ............                                 ',
        '      1 |                       .................................',
        '          0                          0.5                        1'
    ]
    assert lines == list(textplot_str(1/x, 0, 1))

    lines = [
        '-4.4408 |                                                  ......',
        '        |                                       ...........      ',
        '        |                                .......                 ',
        '        |                         .......                        ',
        '        |                    .....                               ',
        '        |                ....                                    ',
        '        |             ...                                        ',
        '        |           ..                                           ',
        '-1.8771 | --------..---------------------------------------------',
        '        |       ..                                               ',
        '        |      /                                                 ',
        '        |     /                                                  ',
        '        |    .                                                   ',
        '        |                                                        ',
        '        |   .                                                    ',
        '        |                                                        ',
        '        |                                                        ',
        '-3.9889 |  .                                                     ',
        '          0                          0.5                        1'
    ]
    assert lines == list(textplot_str(log(x), 0, 1))


def test_sinc():
    x = Symbol('x')
    lines = [
        '0.97729 |                           . .                          ',
        '        |                          /   \\                         ',
        '        |                         .     .                        ',
        '        |                                                        ',
        '        |                        .       .                       ',
        '        |                                                        ',
        '        |                                                        ',
        '        |                       .         .                      ',
        '0.41528 | -------------------------------------------------------',
        '        |                      .           .                     ',
        '        |                                                        ',
        '        |                     .             .                    ',
        '        |      ...                                       ...     ',
        '        |    ..   ..         .               .         ..   ..   ',
        '        |  ..       \\                                 /       .. ',
        '        | /          \\      .                 .      /          \\',
        '        |             ..   /                   \\   ..            ',
        '-0.2169 |               ...                     ...              ',
        '          -10                        0                          10'
    ]
    assert lines == list(textplot_str(sin(x)/x, -10, 10))


def test_imaginary():
    x = Symbol('x')
    lines = [
        '      1 |                                                      ..',
        '        |                                                   ...  ',
        '        |                                                ...     ',
        '        |                                              ..        ',
        '        |                                           ...          ',
        '        |                                         ..             ',
        '        |                                       ..               ',
        '        |                                     ..                 ',
        '0.52941 | ----------------------------------..-------------------',
        '        |                                  /                     ',
        '        |                                ..                      ',
        '        |                               /                        ',
        '        |                              .                         ',
        '        |                                                        ',
        '        |                             .                          ',
        '        |                                                        ',
        '        |                                                        ',
        '      0 |                            .                           ',
        '          -1                         0                          1'
    ]
    assert list(textplot_str(sqrt(x), -1, 1)) == lines

    lines = [
        '      1 |                                                        ',
        '        |                                                        ',
        '        |                                                        ',
        '        |                                                        ',
        '        |                                                        ',
        '        |                                                        ',
        '        |                                                        ',
        '        |                                                        ',
        '0.05882 | -------------------------------------------------------',
        '        |                                                        ',
        '        |                                                        ',
        '        |                                                        ',
        '        |                                                        ',
        '        |                                                        ',
        '        |                                                        ',
        '        |                                                        ',
        '        |                                                        ',
        '     -1 |                                                        ',
        '          -1                         0                          1'
    ]
    assert list(textplot_str(S.ImaginaryUnit, -1, 1)) == lines