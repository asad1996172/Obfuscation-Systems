import input_reader, output_writer, sys

def main(argv):
    input_dir, output_dir = input_reader.read_input_and_output_dir(argv)
    print('Input file is: ' + input_dir)
    print('Output file is: ' + output_dir)
    simplify_corpus(input_dir, output_dir)


def simplify_corpus(in_file, out_file):
    print('Start simplifying corpus')
    with open(in_file) as f:
        for cnt, line in enumerate(f):
            parts = line.split(' ||| ')
            new_line = clear_spaces(parts[1]) + ' - ' + clear_spaces(parts[2])+ '\n'
            if cnt % 100 == 0:
                print('line ' + str(cnt))
            if cnt % 1000 == 0:
                print(new_line)
            output_writer.write_text_to_file(new_line, out_file)
    print('text written')

def clear_spaces(text):
    return text.replace(' ,', ',').replace(' .', '.').replace(' ?', '?').replace(' !', '!').replace('- ', '').replace('-', '')

if __name__ == "__main__":
   main(sys.argv[1:])