
import os

alpha = "abcdefghijklmnopqrstuvwxyz"
apha_up = alpha.upper()
list_dig = [0,1,2,3,4,5,6,7,8,9]
cha = ['"']
cha1 = ["'"]
all_cha = apha_up + alpha + str(list_dig) + str(cha) + str(cha1)


class JsonCsvClass:

   def __init__(self):
      pass

   



   def function_json_to_csv(path_to_json, path_to_csv):
      the_csv = open(path_to_csv+"/your_file.csv", "w")
      datas = ""
      buff1 = open("buffer_file_treat1.txt", "w")
      buff = open("buffer_file.txt", "w")

      with open(path_to_json, "r") as f:
         for line in f:
            buff.write(line)

      buff.close()
   
# let's make use of another file with extension : txt, just cause, there's too much constraints in 
# using directly the json file
  
      buff_read = open("buffer_file.txt", "r")

      for line in buff_read:
         datas += str(line)

      buff_read.close()
   

      print("\n")
      print(datas)
      print("\n")
      dat = datas.replace(",", "")
      print(dat)
      print("\n")
      da = dat.replace(" ", "")
      print(da)
      print("\n")
      d = da.replace(da[(len(da) - 2)], "")
      print(d)
      # d = d.replace(d[(len(d) - 1)], "")
      print("\n")

      all_thing = False
      list_test = ["none", "True"]
      for each in list_test:
         if each in d:
            continue
         else:
            all_thing = True

        
            
      data_normal = datas
      data_without_space = datas = datas.replace(" ", "")
      data_without_double = datas = datas.replace('"', '')

   

      var_lengh = len(datas)
   

      my_list_data = []

      for x in range(0,var_lengh):
      
         if datas[x] == ":":
      # getting keys...
            variable_left = ""
            var_left = ""
            y = x - 1
            while ((datas[y] != ",") and (datas[y] != "{")):
               variable_left += datas[y]
         
               y -= 1

            for v in range(0, len(variable_left)):
               var_left += variable_left[len(variable_left) - (v+1)]
      
            my_list_data.append(str(var_left))






   # Getting all index...
      all_ind = []
      my_registration = {}
      for each in my_list_data:
         each = str(each)
         each = each.replace("\n", "")
         each_in_string = '"'+each+'"'
         all_ind.append(d.find(str(each_in_string)))
         my_registration.update({each: ""})





      global each_block_right
      each_block_right = ""
      val_l = ""
      for each in my_list_data:
         var_r = ""
         each = str(each)
         each = each.replace("\n", "")
         each_in_string = '"'+each+'"'
         if(each_in_string in each_block_right):
            continue
         else:
            val_l += each_in_string
            each_block_right = " "
            after = d.find(each_in_string) + len(each_in_string) + 1
            after_o = after
            if ((each_in_string in d) and (d[after_o] == "{")):
                t = True
                cal = 1
                while t:
                    
                    var_r += d[after_o]
                    after_o += 1

                    if cal == 0:
                       break

                  #   if after_o in all_ind:
                  #       t = False
                    if after_o == len(d):
                       break

                    if d[after_o] == "{":
                        cal += 1
                    if d[after_o] == "}":
                        cal -= 1
                each_block_right += var_r
                    
                       
            elif ((each_in_string in d) and (d[after_o] == "[")):
                t = True
                cal = 1
                while t:
                    
                    var_r += d[after_o]
                    after_o += 1

                    if cal == 0:
                       break

                  #   if after_o in all_ind:
                  #       t = False
                    if after_o == len(d):
                       break

                    if d[after_o] == "[":
                        cal += 1
                    if d[after_o] == "]":
                        cal -= 1
                each_block_right += var_r


            else:
               t = True
               while t:
                    
                    var_r += d[after_o]
                    after_o += 1

                    if after_o in all_ind:
                        t = False
                    if after_o == len(d):
                       break



         if all_thing == True:
            print(val_l +" , "+var_r)
            the_csv.write(val_l +" , "+var_r+"\n")
            val_l = "" 
         else:
            print("Content problem found... ")

                





    





   
      f.close()
      the_csv.close()

      os.remove(buff)
      os.remove(buff1)





















