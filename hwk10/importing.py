import os, sys
import json

# Inserting the parent directory to the path so we can import song file
# located in hwk1 directory
parent_dir = os.path.abspath(os.path.pardir)
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)
from hwk1 import song

"""
The following code presents different ways on how to use json library to decode
and encode a python dictionary. This dictionary has different data types.
The dictionary is imported as a variable, read from a txt file and from a
json file. And also it creates a json file with the dictionary.
The code uses: -dump-, -dumps-, -encoder-.
The dump and dumps serialize the obj as a JSON formatter so it
can be written to a file. The JSONEncoder is the extensible JSON encoder for
python data structures. 
Python -> JSON
The code uses: -load-, -loads-, -decoder-.
The load and loads deserialize the obj to a Python obj so it can be
ready to processed by any python func. The JSONDecoder is a JSON decoder.
JSON -> Python
"""

print("=====JSON Dumps an imported dict variable=====")
json_dumps_dict = json.dumps(song.dictionary, indent=2)
print("json_dumps_dict type: {}".format(type(json_dumps_dict)))
print(json_dumps_dict)

print("=====JSON Loads an imported dict variable=====")
json_loads_dict = json.loads(json_dumps_dict)
print("json_loads_dict type: {}".format(type(json_loads_dict)))
print(json_loads_dict)

print("=====JSON Encodes an imported dict variable=====")
json_encode_dict = json.JSONEncoder(sort_keys=True,
                                    indent=2).encode(song.dictionary)
print("json_encode_dict type: {}".format(type(json_encode_dict)))
print(json_encode_dict)

print("=====JSON Decodes an imported dict variable=====")
json_decoder_dict = json.JSONDecoder().decode(json_encode_dict)
print("json_decoder_dict type: {}".format(type(json_decoder_dict)))
print(json_decoder_dict)

json_path_e = os.path.abspath(os.path.join(os.path.pardir, "hwk10", "song_encode.json"))
print("=====Writing to json file=====")
json_file = open(json_path_e, 'w')
json_file.write(json_encode_dict)
json_file.close()

json_path = os.path.abspath(os.path.join(os.path.pardir, "hwk10", "song_dumps.json"))
print("=====Writing to json file=====")
json_file = open(json_path, 'w')
json_file.write(json_dumps_dict)
json_file.close()

json_path_d = os.path.abspath(os.path.join(os.path.pardir, "hwk10", "song_dump.json"))
print("=====Writing to json file=====")
json_file = open(json_path_d, 'w')
json.dump(song.dictionary, json_file, indent=3)
json_file.close()

print("=====Reading a txt file=====")
txt_path = os.path.abspath(os.path.join(os.path.pardir, "hwk10", "song.txt"))
txt_file = open(txt_path)
lines = ""
for line in txt_file:
    lines = lines + line
txt_file.close()

print("=====JSON Dumps a python dictionary from a txt file after loading it=====")
json_dumps_txt = json.dumps(lines, indent=2)
print("json_dumps_txt type: {}".format(type(json_dumps_txt)))
print(json_dumps_txt)

print("=====JSON Loads a python dictionary from a txt file=====")
json_loads_txt = json.loads(lines, object_hook=dict)
print("json_load_txt type: {}".format(type(json_loads_txt)))
print(json_loads_txt)

print("=====JSON Load json file=====")
json_file = open(json_path)
json_load_json = json.load(json_file)
json_file.close()
print("json_load_json type: {}".format(json_load_json))
print(json_load_json)
print(json_load_json["title"])
print(json_load_json.keys())

print("=====JSON Encoder json file=====")
json_file = open(json_path)
lines = ""
for line in json_file:
    lines = lines + line
json_encoder_json = json.JSONDecoder().decode(lines)
json_file.close()
print("json_encoder_json type: {}".format(type(json_encoder_json)))
print(json_encoder_json)
print(json_encoder_json["title"])
print(json_encoder_json.keys())
