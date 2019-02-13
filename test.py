import filters 

def main(): 
    print('Choose the effect you would like to try (input a number)')
    print('1) Object Filter')
    print('2) Shades of Gray')
    print('3) Negate Red')
    print('4) Negate Green')
    print('5) Negate Blue')
    print('6) Flip Horizontally')
    number = input('Enter a number: ')
    if number == '1': 
        file_1 = input('Enter the name of the first file: ')
        file_2 = input('Enter the name of the second file: ')
        file_3 = input('Enter the name of the third file: ')
        output = filters.object_filter(file_1, file_2, file_3) 
    else: 
        file = input('Enter the name of the file: ')
        if number == '2': 
            output = filters.shades_of_grey(file)
        elif number == '3': 
            output = filters.negate_red(file)
        elif number == '4': 
            output = filters.negate_green(file)
        elif number == '5': 
            output = filters.negate_blue(file) 
        elif number == '6': 
            output = filters.flip_horizontal(file)
    output_file = open('output.ppm', 'w+')
    output_file.write(output)
    print('Output file created!')

main()