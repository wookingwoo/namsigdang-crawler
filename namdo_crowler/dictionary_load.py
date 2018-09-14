import csv

class dataload:
    def load(self):
        path_food = 'Food\\food.csv'
        file = open(path_food, 'r', encoding='euc-kr')
        reader = csv.reader(file)
        dic = {}
        for data in reader:
            dic[data[0] + "breakfast_en"] = data[1]
            dic[data[0] + "lunch_en"] = data[2]
            dic[data[0] + "dinner_en"] = data[3]
        print(dic)
        file.close()
        return dic
