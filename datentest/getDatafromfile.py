
class File(): #funktioniert
    data_to_file = 0
    i = 0
    f = open("testdata2.txt", 'a')
    while i < 10:
        i+1   
        f.writelines('data_to_file')
        data_to_file +1
        if(i == 10):
            f.close()
    