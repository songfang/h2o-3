from __future__ import print_function
import sys
sys.path.insert(1,"../../")
import h2o
from tests import pyunit_utils

def sort():
    #df = h2o.import_file(pyunit_utils.locate("smalldata/synthetic/smallIntFloats.csv.zip"))
    #df = h2o.H2OFrame(python_obj=list(range(0,250000000)))
    #df = h2o.import_file(pyunit_utils.locate("bigdata/laptop/jira/twoColumns.csv"))
    df = h2o.import_file("hdfs://mr-0xd1-precise1.0xdata.loc/datasets/twoColumnsID.csv")
    sorted_column_indices = [0,1]
    df1 = df.sort(sorted_column_indices).asnumeric()
    pyunit_utils.check_sorted_2_columns(df1, sorted_column_indices, prob=0.01)

if __name__ == "__main__":
    pyunit_utils.standalone_test(sort)
else:
    sort()

