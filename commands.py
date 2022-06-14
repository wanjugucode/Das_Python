import csv
from figure import MergeSort
from search import SearchCSV
import click

@click.group()
def main():
   
       pass

def csv_read_details(file_name):
    data = []
    with open(file_name, 'r') as file:
                reader = csv.reader(file)
                header = next(reader)
                for row in reader:
                    data.append(row)
    sorted = MergeSort(data)
    sorted.sortData()
                    

    try:
        print("Writing file...")
        with open(file_name, 'w') as csvfile:
            data_writer = csv.writer(csvfile)
            data_writer.writerow(header)
            data_writer.writerows(data)
        print(f"File created : {file_name}")
    except IOError as e:
        print (f"Couldn't write into {file_name}. Error: {e}")

@click.command(name='sorting')
@click.argument('file_name', type=click.Path(exists=True))
@click.option('--file_name', default='string', help='csv file extension e.g "test.csv"')
def csv_read_and_sort(file_name):
    return csv_read_details(file_name)



# searching through the csv

def search_csv (file_name, target, finder):
    with open(file_name, "r") as file:
        reader = csv.DictReader(file)
        data = list(reader)
        
      
        things = SearchCSV(data,target, finder)
        print(things.search())


@click.command(name='searching')
@click.argument('file_name', type=click.Path(exists=True), nargs = 1)
@click.argument('target', nargs = 1)
@click.argument('finder',nargs = 1)
@click.option('--target', default='string', help='the value of the finder i.e "NULL" from id')
@click.option('--finder', default='string', help='key of the target i.e "Id, ImageSrc"')
def csv_search(file_name, target, finder):
    return search_csv(file_name, target, finder)



    
main.add_command(csv_read_and_sort,'sorting')
main.add_command(csv_search,'searching')

if __name__ == "__main__":
    main()