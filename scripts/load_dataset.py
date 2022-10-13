from users.models import Tab
import csv

def run():
    with open('tabulado.csv') as file:
        reader = csv.reader(file)
        next(reader)

        Tab.objects.all().delete()

        for row in reader:
            print(row)

            tabmodel = Tab(
                month=row[0],
                year=row[1],
                food=row[2],
                brewery=row[3],
                chemical_products=row[4],
                other_manufactures=row[5],
                textiles_leather=row[6],
                total=row[7],
            )
            tabmodel.save()
            
