import pandas as pd
import pytest

@pytest.fixture
def sample_output():
    test_output = pd.read_excel(r"tests\fixtures\invoiceReportNovember2015.xlsx")
    test_output.rename({"is Finalized?": "isFinalized"}, axis=1, inplace=True)
    return test_output

@pytest.fixture
def actual_output():
    output = pd.read_excel(r"outputs\report.xlsx")
    return output

def test_counts(sample_output, actual_output):
    sample_counts = len(sample_output)
    actual_counts = len(actual_output)
    assert sample_counts == actual_counts, f"Sample counts: {sample_counts} vs Actual counts: {actual_counts}"

def test_number_of_columns(sample_output, actual_output):
    sample_columns = len(sample_output.columns)
    actual_columns = len(actual_output.columns)
    assert sample_columns == actual_columns, f"Sample number of columns: {sample_columns} vs number of columns: {actual_columns}"

def test_schema(sample_output, actual_output):
    data_types_check = (sample_output.dtypes.sort_index() == actual_output.dtypes.sort_index())
    assert len(data_types_check.loc[data_types_check == False].index.to_list()) == 0, "Different data types"

def test_column_is_same(sample_output, actual_output):
    sample_columns = sorted(sample_output.columns)
    actual_columns = sorted(actual_output.columns)
    assert sample_columns == actual_columns, "Different columns"

def test_is_same(sample_output, actual_output):
    assert actual_output.equals(sample_output), "The two dataframes differ"
