import datetime
import glob2

# globbing all txt file extenstion contents and printing in new file created with timestamp
filenames = glob2.glob('*.txt')
print(filenames)
with open(datetime.datetime.now().strftime("%d-%m-%Y,%H:%M:%S") + '.txt', 'w') as file:
    for filename in filenames:
        with open(filename, 'r') as f:
            file.write(f.read() + '\n')
