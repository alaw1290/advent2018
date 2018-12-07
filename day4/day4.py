# day 4 challenge
from datetime import datetime

def main():

    input_data = {}

    with open('input_sample.txt','r') as file:
        for line in file:
            line = line.strip()
            timestamp = datetime.strptime(line[1:17], '%Y-%m-%d %H:%M')
            update = line[]
if __name__ == '__main__':
    main()