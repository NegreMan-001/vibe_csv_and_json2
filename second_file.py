
import os
from csv_json import JsonCsvClass


# second function

def function_first(path_json, path_csv):
    datas = ""
    buff = open("buffer_file.txt", "w")

    if path_json.endswith(".json"):
      # test_constraint = 0
      # if datas.startswith("{") and datas.endswith("}"):
      #    test_constraint += 1
      # else:
      #    test_constraint -= 1

      # if (datas.find("None") > 0 or datas.find("True") > 0 or datas.find("False") > 0):
      #    test_constraint -= 1

      # if test_constraint > 1:
       # my_ins = JsonCsvClass
        JsonCsvClass.function_json_to_csv(path_json, path_csv)
      # else:
      #    print("Problem with datas... ")
    else:
        print("Problem file extension...")




    os.remove(buff)
