def read_file(file): 
    f = open(file, "r")
    data = f.read()
    data_split = data.split('\n')
    pure_file = [] 
    for row in data_split[3:]: 
        split = row.split(' ')
        for num in split: 
            if num != '': 
                pure_file.append(num)
    return {
        "PPM_encoding": data_split[0], 
        "Columns": data_split[1].split(' ')[0],
        "Rows": data_split[1].split(' ')[1],
        "Max_color_value": data_split[2],
        "File": pure_file 
    }

def object_filter(file1, file2, file3): 
    one = read_file(file1)
    two = read_file(file2)
    three = read_file(file3)
    return_file = one["PPM_encoding"] + "\n" + one["Columns"] + " " + one["Rows"] + "\n" + one["Max_color_value"] + "\n"
    counter = 0
    while counter < len(one["File"]): 
        # Only if image 1 has the object should the return_file contain pixels from anything but image 1 
        if one["File"][counter] != two["File"][counter] and one["File"][counter] != three["File"][counter]: 
            return_file += two["File"][counter] + "   "
        else:  
            return_file += one["File"][counter] + "   "
        counter += 1 
    return return_file 
    
def flip_horizontal(file): 
    parsed = read_file(file)
    return_file = parsed["PPM_encoding"] + "\n" + parsed["Columns"] + " " + parsed["Rows"] + "\n" + parsed["Max_color_value"] + "\n"
    counter = 1
    rows = [] 
    row = []
    pixel = []
    for pix in parsed["File"]: 
        pixel.append(pix) 
        if counter % 3 == 0: 
            row.append(pixel)
            pixel = [] 
        if counter % (int(parsed["Columns"])*3) == 0: 
            rows.append(row)
            row = [] 
        counter += 1 
    for row in rows: 
        counter = len(row) - 1 
        while counter >= 0: 
            pixel = row[counter] 
            return_file += pixel[0] + "   " + pixel[1] + "   " + pixel[2] + "   " 
            counter -= 1 
    return return_file 

def shades_of_grey(file): 
    parsed = read_file(file)
    return_file = parsed["PPM_encoding"] + "\n" + parsed["Columns"] + " " + parsed["Rows"] + "\n" + parsed["Max_color_value"] + "\n"
    counter = 1
    for pix in parsed["File"]: 
        if counter % 3 == 0: 
            average = str(round((int(pix) + int(parsed["File"][counter - 1]) + int(parsed["File"][counter - 2]))/3)) 
            return_file += average + "   " + average + "   " + average + "   "
        counter += 1
    return return_file 

def negate(file, color): 
    parsed = read_file(file)
    return_file = parsed["PPM_encoding"] + "\n" + parsed["Columns"] + " " + parsed["Rows"] + "\n" + parsed["Max_color_value"] + "\n"
    counter = color 
    for pix in parsed["File"]: 
        if counter % 3 == 0: 
            return_file += (str(int(parsed["Max_color_value"]) - int(pix)))
        else: 
            return_file += pix 
        return_file += "   " 
        counter += 1
    return return_file 

def negate_red(file): 
    negated = negate(file, 1)
    return negated 

def negate_green(file): 
    negated = negate(file, 2)
    return negated 

def negate_blue(file): 
    negated = negate(file, 3)
    return negated 

