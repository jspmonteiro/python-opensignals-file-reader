# -*- coding: utf-8 -*-

"""
.. module:: opensignalsfilereader

Created on Fri Jan 26 11:48:06 2018

@author: Joana

"""

import numpy as np 
import json


def OpenSignalsFileReader (file):
    
    """
    Parameters
    -------
    file
        Name of the file for analysis.

    Returns
    -------
    header : JSON object
    data : array
    t : array
        
    """

    header = {}
    
    #Start acquisition of the header from file
    with open(file) as f:
        line = f.readline()
        cnt = 0
        headerlines = 3

        while line:
            if cnt <= headerlines:
                header[cnt] = line[2:]
            line = f.readline()
            cnt += 1
    
    #Define header
    header = json.loads(header[1])
    
    devices = header[header.keys()[0]]

    #Read "Sampling Rate" from header
    s_rate = devices['sampling rate']

    #Load data from file
    data = np.loadtxt(file)

    #Calculate the time line
    t = np.arange(len(data)) / float(s_rate) 
    
    return (data, t, header)

if __name__ == '__main__':
    
    filename = "FILE_NAME.txt"
    
    #shows the content of the file read
    
    print (' Header:')
    print(OpenSignalsFileReader(filename)[2])

    print ('\n Extracted Data:')
    print(OpenSignalsFileReader(filename)[0])
    
    print ('\n Time line:')
    print(OpenSignalsFileReader(filename)[1])
