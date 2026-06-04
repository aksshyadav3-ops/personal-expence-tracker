import csv
import os
import datetime
datafile="expences.csv"
def add_data():
    with open(datafile,"a",newline="") as file:
        cost= input("enter the cost: ")
        catr= input("enter the category of the expense: ")
        note= input("enter note (optional): ")
        if(note=="no"):
            note="N/A"
        date= datetime.date.today().strftime("%Y-%m-%d")
        file_exists=os.path.exists(datafile)
        writer=csv.writer(file)
        if not file_exists:
            writer.writerow(["COST","CATEGORY","NOTE","DATE"])

        writer.writerow([cost,catr,note,date])
        print("Expence record added successfully")
        file.flush()


def view_expence():
    with open(datafile,"a",newline="") as file:
        reader=csv.reader(file)
        print("COST  CATEGORY  NOTE  DATE")
        total=0 
        for row in reader:
            cost,catr,note,date= row
            total+=cost
            print(cost,"  ",catr,"  ",note,"  ",date)
        print("the total cost spend is: ",total)


def filter_expence():
    catr= input("enter the category you want to see (food,entertainment,others): ")
    with open(datafile,"a",newline="") as file:
        reader=csv.reader(file)
        s1,s2,s3=0
        def foodexpence():
            for row in reader:
                if(row[1]=="food"):
                    print(row)
                    s1+=float(row[0])
            print("The subtotal for food is: ",s1)        

        def entexpence():
            for row in reader:
                if(row[1]=="entertainment"):
                    print(row)
                    s2+=float(row[0])

        def others():
            for row in reader:
                if(row[1]=="others"):
                    print(row)
                    s3+=float(row[0])
        
        choice= input("Select an option for category: ")
        if choice=="food": foodexpence()
        if choice=="entertainment": entexpence()
        if choice=="others": others()


def main():
    while True:
        print("---------/ PERSONAL EXPENCE TRACKER /---------")
        print("1. Add expense")
        print("2. View all expence")
        print("3. filter by category")
        print("4. Exit")
        choice= input("Select an option: ")
        if choice =="1": add_data()
        if choice =="2": view_expence()
        if choice =="3": filter_expence()
        if choice =="4":
            print("goodbye!")
            break
        
if __name__== "__main__":
    main()        