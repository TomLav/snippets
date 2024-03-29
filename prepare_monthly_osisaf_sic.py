"""
   Python script to run monthly average SIC notebook from the command-line, using papermill
"""

import sys
import papermill as pm
from datetime import date
from dateutil.relativedelta import *

def run_notebook(area, dt, outdir, indirs=None):
    notebook = 'Prepare Monthly OSISAF SIC.ipynb'
    notebook_out = notebook.replace('.ipynb','_out.ipynb')

    notebook_par = {'area': area, 'dt': dt, 'outdir': outdir,}
    if indirs is not None:
        notebook_par['indirs'] = indirs

    print("Call {} with params\n\t{}".format(notebook, notebook_par))

    _ = pm.execute_notebook(notebook,notebook_out,parameters=notebook_par)


if __name__ == '__main__':
    import argparse

    # prepare and parse parameters to the script
    parser = argparse.ArgumentParser(prog='prepare_monthly_osisaf_sic.py',
                                     description='Prepare monthly product files for the OSI SAF SIC CDR v3 (OSI-450-a,OSI-430-a)')
    parser.add_argument('AREA', choices=('nh','sh'), help='Hemisphere for which to compute the monthly SIC product')
    parser.add_argument('MONTH', help='Datestring YYYYMM (or YYYYMMDD for any day in the month) for which to compute the monthly SIC product. Can also be "PREV" for previous month.')
    parser.add_argument('-o', help='Directory where to write the monthly SIC file', default='.')
    parser.add_argument('-i', help='JSON file with paths to the input directories where to fine daily SIC files.', default=None)
    args = parser.parse_args()

    # handle MONTH == PREV
    month = args.MONTH
    if month.upper() == 'PREV':
        month = date.today() - relativedelta(months=1)
        month = '{:%Y%m}'.format(month)

    # run the monthly average via the notebook
    try:
        run_notebook(args.AREA, month, args.o, args.i)
    except pm.exceptions.PapermillExecutionError as pme:
        print(pme)
        sys.exit("Failed with Papermill Execution Error")
    except Exception as ex:
        print(ex)
        sys.exit("Failed with general exception.")

