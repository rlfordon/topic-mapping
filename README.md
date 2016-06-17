# topic-mapping

This is an experimental Python script that will convert JSON outputs from courtlistener.com into a directory of text files.  This directory will then be suitable for ingesting into topic-mapping software such as the Stanford Natural Language Processing Group's Topic Modeling Tool. 

To use, ensure that you have a directory of json files.  Then, while in the same top-directory that contains the folder of JSON files, run jsontotext.py in the command line.  The result will be a folder of opinion text files. 

Note that this script uses the lxml module, so it will be necessary to install that first.

If you have any questions or comments please contact me! 
