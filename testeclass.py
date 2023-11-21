
class CsvToJson:

    def __init__(self):
        pass




    def csvJson(fcsv,fjson): 
    #verifikasyon ekstansyon fichye a
        if not fcsv.endswith('.csv'):
            print(f"Le fichier {fcsv} n'a pas l'extension .csv. Veuillez fournir un fichier CSV.")
            return

        with open(fcsv, 'r') as csv_file:
            liy = csv_file.readlines()
            diks={}
            for eleman in liy:
                separe= eleman.strip().split(',')

                # itilize tout premye eleman yo pou kle
                kle = separe[0]

                # Utilize res eleman yo pou vale
                val = separe[1:]

                # Ajoute kle ak vale yo nan diksyone a
                diks[kle] = val
            
          

        with open(fjson+"/file_json.json", 'w') as json_file:
            json_file.write(str(diks))


    


        