def animal_file(file):
    try:
        with open(file, 'r') as f_obj:
            print("\nIn " + file + " name are-")
            lines = f_obj.readlines()
            for line in lines:
                print(line.strip())
    except:
        pass

files = ['cats.txt', 'dogs.txt', 'another.txt']
for file in files:
    animal_file(file.title())