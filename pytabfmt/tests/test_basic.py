import pytest
import glob
import os
import filecmp
import io
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import pytabfmt as ptf

fixtures_dir = os.path.join(os.path.dirname(__file__), 'fixtures')

@pytest.fixture()
def example_table():
    path = os.path.join(fixtures_dir, 'example_table_1.txt')
    return path


@pytest.fixture()
def example_table_with_missing_data():
    path = os.path.join(fixtures_dir, 'example_table_2.txt')
    return path


def test_simple_filewrite(example_table, tmpdir):
    example = example_table
    tbl = ptf.LatexTable('Teacher Kyle Adi Vincent'.split(),
                         ['%s', '%0.2f', '%0.2f', '%0.2f'])
    tbl.add_row(['DB', 0.0, 0.0, 5.0])
    tbl.add_row(['Swan', 5.0, 5.0, 0.0])
    tbl.add_row(['Bazant', 5.0, 5.0, 0.0])

    fpath = tmpdir.join('test.txt')
    tbl.write(fpath)

    assert filecmp.cmp(fpath, example)


def test_simple_filewrite_missing_data(example_table_with_missing_data, tmpdir):
    example = example_table_with_missing_data
    tbl = ptf.LatexTable('Teacher Kyle Adi Vincent'.split(),
                         ['%s', '%0.2f', '%0.2f', '%0.2f'])
    tbl.add_row(['DB', 0.0, 0.0, 5.0])
    tbl.add_row(['Swan', 5.0, 5.0, 0.0])
    tbl.add_row(['Bazant', 5.0, 5.0, None])

    fpath = tmpdir.join('test.txt')
    tbl.write(fpath)

    assert filecmp.cmp(fpath, example)
