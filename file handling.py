try:
    f = open(xfile.txt,'w')
    f.write("checking how file handling works")
except:
    print("look's like its not working")
finally:
    print("anyways, i am always exexcuted")


