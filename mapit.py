import webbrowser, sys

# sys.argv stores a list of a programs's filename and command line arguments
# If its length is greater than 1, then a command line argument has been provided
# We need to use the join() method as sys.argv is a list of strings and [1:] to chop off 1st elemetn in the array which is the filename
address = ""

if len(sys.argv) > 1:
    # Get address fro command line
    address = ' '.join(sys.argv[1:]) 



webbrowser.open('https://www.google.com/maps/place/' + address)



