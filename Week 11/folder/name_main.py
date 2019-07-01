print("This always be executed!")

def main():
    print("First module's name is:{}".format(__name__))

print(__name__)

if __name__=="__main__":
    print("Run directly.")
    main()
else:
    print("Run from import")
