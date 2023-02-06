# -*- coding: utf-8 -*-
"""Launch a calculation using the 'diff-tutorial' plugin"""
from pathlib import Path

from aiida import engine, orm
from aiida.common.exceptions import NotExistent

#INPUT_DIR = Path(__file__).resolve().parent / 'input_files'
INPUT_DIR = Path(__file__).resolve().parent

# Create or load code
computer = orm.load_computer('localhost')
try:
    code = orm.load_code('opt@localhost')
except NotExistent:
    # Setting up code via python API (or use "verdi code setup")
    code = orm.Code(label='opt', remote_computer_exec=[computer, '/home/clarkszw/envs/aiida/bin/python3'], input_plugin_name='optimization')

# Set up inputs
builder = code.get_builder()
builder.atom = orm.SinglefileData(file=INPUT_DIR / 'N2')
# String = orm.DataFactory("string")
# builder.basis = String(input_string = "ccpvdz").store()
builder.basis = Str("ccpvdz")
builder.metadata.description = 'Test job submission with the optimization plugin'

# Run the calculation & parse results
result = engine.run(builder)
optimized = result['opt'].get_content()
print(f'The optimized structure is::\n{optimized}')

# Submit calculation to the aiida daemon
# node = engine.submit(builder)
# print("Submitted calculation {}".format(node))
