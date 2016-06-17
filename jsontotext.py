import os
import json
from lxml import html

# create list of text filepaths
json_paths = [] 
json_dir = input('Please enter directory of JSON files:  ')
for subdir, dirs, files in os.walk(json_dir):
    for file in files:
        #print os.path.join(subdir, file)
        filepath = subdir + os.sep + file

        if filepath.endswith(".json"):
            json_paths.append(filepath)

# create new directory for text files
text_dir = json_dir+'_txt'
os.mkdir(text_dir) 

for json_path in json_paths: 
    # following code is done for each json file 
    # JSON to plaintext 
    with open(json_path) as json_file:
        data = json.load(json_file)
        blob = data['html_with_citations']
        doc = html.fromstring(blob)
        text = doc.text_content()
        text = text.encode('ascii','ignore')
        text_name = os.path.split(json_path)[1].split('.')[0]+'.txt'
        text_path = os.path.join(text_dir,text_name)  #filepath for json doc
    text = str(text)
    with open(text_path, 'w') as text_file: 
        text_file.write(text)
        text_file.close()