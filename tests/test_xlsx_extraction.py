#!/usr/bin/env python
"""
Test xlsx extraction
"""

import hashlib, os
from asrtoolkit.extract_excel_spreadsheets import proc_input_dir_to_corpus


def test_excel_conversion():
  " execute single test "

  proc_input_dir_to_corpus("../samples", "corpus")
  assert (os.path.exists("corpus/FinancialStatementFY18Q4.txt"))


if __name__ == '__main__':
  import sys
  import pytest
  pytest.main(sys.argv)
