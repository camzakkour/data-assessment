log_file = open("um-server-01.txt")

# defining a sales_report function
def sales_reports(log_file):
    #basic for loop to take each line of the file
    for line in log_file:
        #Allows the text on lines to remove white space between them
        line = line.rstrip()
        #variable that specifies that the first 3 elements are considered 'day'
        day = line[0:3]
        #checks to see if any of the lines have the first 3 elements as 'Tue' if they do then print out the entire line that it is on
        if day == "Mon":
            print(line)



sales_reports(log_file)
