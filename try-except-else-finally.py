def process_file(filename):
    try:
        fi = open(filename, 'r')
    except IOError:
        print('Oops: couldn\'t open {} for reading' .format(filename))
        return
    else:
        lines = fi.readlines()
        print('{} has {} lines.' .format(filename, len(lines)))
        fi.close()
    finally:
        print('Done with file {}' .format(filename))

    print('The first line of {} is:\n{}' .format(filename, lines[0]))
    return

process_file('sonnet0.txt')
process_file('sonnet18.txt')
