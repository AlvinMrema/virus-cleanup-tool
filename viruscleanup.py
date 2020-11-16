import os, shutil


LOGS_FILENAME  = "logs.txt"

# Useful Variables
all_folders = []  # List of folders from the main folder and it's subfolders
fileCount = 0
folderCount = 0

# File used to log status and error messages
logFile = None


# Setup a custom file for writing logs and statuses
def setupLogs ():
    global logFile
    logFile = open(LOGS_FILENAME, "w")


# Display a message to the user. By default, end is a new line character
def display ( message, end = "\n" ):
    print(message, end=end)


# Save a message to a logs file. By default, end is a new line character
def log ( message, end = "\n" ):
    global logFile
    logFile.write(message)
    logFile.write(end)


# Display a message to the user and save the message to a logs file. By 
# default, end is a new line character
def displayAndLog ( message, end = "\n" ):
    global logFile
    logFile.write(message)
    logFile.write(end)

    print(message, end=end)


def filenameChanger(folder, changeFrom, changeTo):
    # Variables for tracking counts
    folders = []
    files = 0

    for folderName, subfolders, filenames in os.walk(os.path.join(os.getcwd(), folder)):
        for subfolder in subfolders:
            folders.append(subfolder)
        
        for filename in filenames:
            if filename[len(filename) - 3:] == changeFrom:
                renameFrom = os.path.join(folderName, filename)
                newFilename = filename[:len(filename) - 3] + changeTo
                renameTo = os.path.join(folderName, newFilename)
                shutil.move(renameFrom, renameTo)
                
                log("{} is changed to {}".format(filename, newFilename))
        
            files += 1
        
    displayAndLog("{} Subfolders and {} Files where found.".format(len(folders), files))