import pytest, json
from ss import SpreadsheetAPI

spreadsheet = SpreadsheetAPI(spreadsheet_id = '1ouvV9yUfjcoMcFnRFzNUZlthoDFhQAY2etfsX3ylY6o', sheet_title = 'Лист2', sheet_id = '0', credentials = 'teat-project-1-951b833b615e.json', apis = 'https://www.googleapis.com/auth/spreadsheets.readonly')
print(spreadsheet.get_sheet())

def test_get_sheet():
    assert spreadsheet.get_sheet()['values'] == [['1', '2', '3'], ['a', 'bb', 'ccc']]


"""def test_get():
    pass


def test_insert():
    pass


def test_clear():
    pass


def test_get_sheet_url():
    pass
"""
