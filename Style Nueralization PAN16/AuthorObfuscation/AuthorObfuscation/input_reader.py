import sys, getopt

def read_input_and_output_dir(argv):
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print('test.py -i <inputfile> -o <outputdir>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('test.py -i <inputdir> -o <outputdir>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputdir = arg
        elif opt in ("-o", "--ofile"):
            outputdir = arg
    return (inputdir, outputdir)

def read_argument_value(argv, argument_name):
    argument_value = None
    print('reading option ' + argument_name)
    opts = ''
    try:
        opts, args = getopt.getopt(argv,'i:s:')
    except getopt.GetoptError as err:
        print('option not found: ' + argument_name)
        print(err)
        return argument_value
    for opt, arg in opts:
        if opt == '-h':
            print('test.py -i <inputdir>')
            sys.exit()
        elif opt in ('-'+argument_name):
            argument_value = arg        
    return argument_value


def read_input_dir(argv):
    return read_argument_value(argv, 'i')
    # try:
    #    opts, args = getopt.getopt(argv,"hi:",["ifile="])
    # except getopt.GetoptError:
    #    print('test.py -i <inputfile>')
    #    sys.exit(2)
    # for opt, arg in opts:
    #    if opt == '-h':
    #       print('test.py -i <inputdir>')
    #       sys.exit()
    #    elif opt in ("-i", "--ifile"):
    #       inputdir = arg      
    # return inputdir


def read_input_file(input_file):
    print('Reading input file ' + input_file)
    with open(input_file, 'r', encoding='utf-8') as f:
        s = f.read()        
    return s