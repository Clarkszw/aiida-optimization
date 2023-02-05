from setuptools import setup

setup(
    name='aiida-optimization',
    packages=['aiida_optimization'],
    entry_points={
        'aiida.calculations': ["optimization = aiida_optimiaztion.calculations:OptCalculation"],
        'aiida.parsers': ["optimization = aiida_optimization.parsers:OptParser"],
    }
)
