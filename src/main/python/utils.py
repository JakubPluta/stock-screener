
# Function for flattening json
# Source: https://www.geeksforgeeks.org/flattening-json-objects-in-python/
# https://medium.com/@augustin.goudet/introduction-to-finnhub-97c2117dd9a9

import pandas as pd
import openpyxl
from openpyxl.worksheet.dimensions import ColumnDimension, DimensionHolder
from openpyxl.utils import get_column_letter
from openpyxl.utils.dataframe import dataframe_to_rows
from openpyxl.styles.differential import DifferentialStyle
from openpyxl.formatting.rule import Rule
from openpyxl.styles import Border, Side, Font, PatternFill


def flatten_json(y):
    out = {}
    def flatten(x, name =''):

        # If the Nested key-value
        # pair is of dict type
        if type(x) is dict:

            for a in x:
                flatten(x[a], name + a + '_')

                # If the Nested key-value
        # pair is of list type
        elif type(x) is list:

            i = 0

            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x

    flatten(y)
    return out


def fit_width(ws):
    dim_holder = DimensionHolder(worksheet=ws)
    for col in range(ws.min_column, ws.max_column + 1):
        dim_holder[get_column_letter(col)] = ColumnDimension(ws, min=col, max=col, width=18)
    ws.column_dimensions = dim_holder


def write_data_frame_to_rows(ws, data, header=True):
    for r in dataframe_to_rows(data, index=True, header=header):
        ws.append(r)
    fit_width(ws)


def format_ws(ws):
    grey_background = PatternFill(bgColor="90EE90")

    header = DifferentialStyle(font=Font(bold=True))
    background_color = DifferentialStyle(fill=grey_background)

    r0 = Rule(type="expression", dxf=header)
    r1 = Rule(type="expression", dxf=background_color)

    r0.formula = ["ISBLANK($A1)=False"]
    r1.formula = ["ISBLANK($A1)=False"]
    ws.freeze_panes = ws["B2"]

    last_row = ws.max_row
    last_column = get_column_letter(ws.max_column)

    ws.conditional_formatting.add(f"A1:{last_column}1", r0)
    ws.conditional_formatting.add(f"A1:{last_column}{last_row}", r1)
    format_ws_borders(ws)


def format_ws_borders(ws):
    border = Border(left=Side(border_style='medium', color='000000'),
                    right=Side(border_style='medium', color='000000'),
                    top=Side(border_style='medium', color='000000'),
                    bottom=Side(border_style='medium', color='000000'))

    rows = ws
    for row in rows:
        for cell in row:
            cell.border = border

