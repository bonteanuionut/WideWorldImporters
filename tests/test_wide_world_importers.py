import pandas as pd
import pytest

@pytest.fixture
def sample_output():
    test_output = pd.read_excel(r"tests\fixtures\invoiceReportNovember2015.xlsx")
    return test_output

@pytest.fixture
def actual_output():
    output = pd.read_csv(r"outputs\report.csv")
    return output

@pytest.mark.skip(reason="")
def test_counts(sample_output, actual_output):
    sample_counts = sample_output.count()
    actual_counts = actual_output.count()
    assert sample_counts == actual_counts, f"Sample counts: {sample_counts} vs Actual counts: {actual_counts}"

@pytest.mark.skip(reason="Unde development")
def test_schema(sample_output, actual_output):
    pass

@pytest.mark.skip(reason="")
def test_columns_is_same(sample_output, actual_output):
    sample_columns = sample_output.columns
    actual_columns = actual_output.columns
    assert sample_columns == actual_columns, "Different columns"

@pytest.mark.skip(reason="")
def test_is_same(sample_output, actual_output):
    assert actual_output.equals(sample_output), "The two dataframes differ"
