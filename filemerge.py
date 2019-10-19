import sys
import os

def joinfile(fromdir, filename, todir):
    if not os.path.exists(todir):
        os.mkdir(todir)
    if not os.path.exists(fromdir):
        print('Wrong directory')
    outfile = open(os.path.join(todir, filename), 'wb')
    files = os.listdir(fromdir)  # list all the part files in the directory
    files.sort()  # sort part files to read in order
    for file in files:
        filepath = os.path.join(fromdir, file)
        infile = open(filepath, 'rb')
        data = infile.read()
        outfile.write(data)
        infile.close()
    outfile.close()


if __name__ == '__main__':
        fromdir = input('分割文件放哪儿了?')
        todir = input('文件要放哪儿?')
        filename = input('合并的文件要叫啥?')      

        try:
            joinfile(fromdir, filename, todir)
        except:
            print('Error joining files:')
            print(sys.exc_info()[0], sys.exc_info()[1])
