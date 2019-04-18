import os
import re
import yaml
from pathlib import Path
from distutils.dir_util import copy_tree
import json
from collections import namedtuple

cwd = os.path.dirname(os.path.realpath(__file__)).replace("\\", "/")
from_dir = f"D:/T3/Git/nofakingway_hugo/content"
content_dir = f"{cwd}/content"
copy_tree(from_dir, content_dir)
for subdir, dirs, files in os.walk(from_dir):
    for file in files:
        if ".md" in file:
            to_path = subdir.replace("\\", "/").replace(from_dir, content_dir)
            slug = (to_path.replace(content_dir, "") + "/" + file.replace(".md", ""))
            with open(subdir + "/" + file) as f:
                content = f.read()
                split_content = content.split("---\n")
                if len(split_content) < 2:
                    print(slug)
                    continue
                start = split_content[1]

                front_matter = yaml.load(start)
                if not front_matter:
                    print(slug)
                    continue
                if 'path' in front_matter:
                    # print("PATH:", front_matter['path'])
                    pass
                    # TODO: compare and Update path?
                else:
                    # print(start)
                    front_matter['path'] = slug
                    front_matter_string = yaml.dump(front_matter).replace("{", "").replace("}", "")
                    split_content[1] = front_matter_string
                    if "{" in front_matter_string:
                        print(slug)
                        print(front_matter_string)
                    joined_content = ("---\n").join(split_content).replace("\n\n\n", "\n\n")
                    if not os.path.isdir(to_path):
                        os.mkdir(to_path)
                    f_write = open(to_path + "/" + file, 'w+')
                    f_write.write(joined_content)
                    f.close
