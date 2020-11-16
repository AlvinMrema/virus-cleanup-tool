'''
 * Copyright: STEM Loyola
 * Date     : September 2019
 * ID       : 2019-P1
 * Level    : Experienced
 *
 *Background: Your flash disk with important school files was infected by LHS
 *            virus. You have successfully scanned and removed the virus from
 *            all folders in the flash disk. However, you have noticed that one
 *            defect was not fixed by the Antivirus program. The virus converted
 *            all your Text (“[filename].txt”) files to an unknown LHS format
 *            (“[filename].lhs”). When you inspected one of the files, you
 *            discovered that the filename and contents were not modified. The
 *            virus just changed the extension from “.txt” to “.lhs”. Changing
 *            back the extension to “.txt” fixes the issue. A quick search of
 *            the flash disk indicates that you have more than 10,000 text files
 *            spread over more than 100 folders. It is going to be impractical
 *            to rename all the files manually.
 *
 * Objective: The flash disk contents are in a folder named “flash-disk”. Create
 *            a program that can visit each folder and its subfolders in the
 *            “flash-disk” and rename all “.lhs” files to “.txt”. Once done,
 *            display how many folders were visited and how many affected files
 *            were fixed by your program.
 *
 *      Note: (1) A folder can contain other folders that contain other folders,
 *                etc.
 *            (2) A folder can be empty.
 *            (3) A folder can contain PDFs, MS Word, MS Excel and LHS files.
 *                Your program should ONLY fix the LHS files.
 *
 *   Version: Python 3
 *
 * Solved By: <Alvin Chris Mrema>
 *     Email: <sonalpha023@gmail.com>
 *     Form : <Alumni>
 *    Stream: <PCM>
'''

import os
import viruscleanup as lhs


def main():
    lhs.setupLogs()

    # Display and log test messages
    lhs.displayAndLog("Starting the process.")

    lhs.log("Current path: ", end="")
    lhs.log(os.getcwd())

    folderName = input('Enter the Name of the folder to work on:')

    lhs.filenameChanger(folderName, 'lhs', 'txt')

    lhs.display("Done!")

    # NOTE: No functionality/logic should be written in this main file. Create
	#       functions inside viruscleanup files for that. "viruscleanup.h"
	#       should contain function declarations ONLY and "viruscleanup.cpp"
	#       should contain the definitions of those functions. This main file
	#       should ONLY contain calls to those functions. Failure to follow
	#       this organization will lead to loss of points. [Remove this comment once read]


if __name__ == "__main__":
    main()