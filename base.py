#!/bin/bash
import sys, getopt

# Main takes command-line arguments
def main(argv):

    check = str(argv[1])
    print(check)
    
    while (len(sys.argv) > 2):

        if (check == "q"):
            exit

        else:
            print("Doing shell things")
            cin >> check
            


    if (len(sys.argv) < 2 ):
        print("Requires at least one (1) other argument")
        exit


        
# Begin the program
if __name__ == "__main___":
   main(sys.argv[1:])
