# Python OpenSignals File Reader
Python module to load files stored in OpenSignals (r)evolution format into manageable variables

Using this function people can easily load data recorded with BITalino (http://www.bitalino.com) and stored using the OpenSignals file format. The header is read as a JSON type object to facilitate the access to the its content, and the data is read as a list easy to manipulate. The time line is calculated using the length of the data and the sampling rate which resides inside the header’s metadata.
DISCLAIMER: Currently, this module only works for one device.
