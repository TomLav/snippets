"""
   Python script to run monthly average SIC notebook from the command-line, using papermill
"""

import papermill as pm
from datetime import date

def run_notebook(area, dt):
    notebook = 'Prepare Monthly OSISAF SIC.ipynb'
    notebook_out = notebook.replace('.ipynb','_out.ipynb')
    notebook_par = {'area': area, 'dt': dt}
    _ = pm.execute_notebook(notebook,notebook_out,parameters=notebook_par)

if __name__ == '__main__':
    import argparse

    # prepare and parse parameters to the script
    parser = argparse.ArgumentParser(prog='prepare_monthly_osisaf_sic.py',
                                     description='Prepare monthly product files for the OSI SAF SIC CDR v3 (OSI-450-a,OSI-430-a)')
    parser.add_argument('AREA', choices=('nh','sh'), help='Hemisphere for which to compute the monthly SIC product')
    parser.add_argument('DATETIME', help='Datestring (YYYYMM or YYYYMMDD) for any day in the month for which to compute the monthly SIC product')
    args = parser.parse_args()

    # run the monthly average via the notebook
    run_notebook(args.AREA, args.DATETIME)

