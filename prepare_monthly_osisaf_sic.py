"""
Python script to explore running a notebook with command-line parameters
using papermill.
"""

import papermill as pm
from datetime import date

notebook = 'Prepare Monthly OSISAF SIC.ipynb'
notebook_out = notebook.replace('.ipynb','_out.ipynb')
notebook_par = {'area': 'sh', 'dt': '201001'}
_ = pm.execute_notebook(notebook,notebook_out,parameters=notebook_par)

