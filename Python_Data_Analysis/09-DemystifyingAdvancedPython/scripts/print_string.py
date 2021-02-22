"Example script to illustrate the use of __main__"

MY_STRING = "hello !"


# This section is only run when running the script
if __name__ == "__main__":
    MY_STRING = "goodbye"
    print("My string is: ", MY_STRING)