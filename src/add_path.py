import os
import re
import yaml
from pathlib import Path
cwd = os.getcwd()
content_dir = f"{cwd}/src/pages"
for subdir, dirs, files in os.walk(content_dir):
    for file in files:
        if ".md" in file:
            slug = (subdir.replace(content_dir, "") + "/" + file.replace(".md", "")).replace("\\", "/")[1:]
            with open(subdir + "/" + file) as f:
                content = f.read()
                split_content = content.split("---")
                start = split_content[1]
                front_matter = yaml.load(start)
                if 'path' in front_matter:
                    # print("PATH:", front_matter['path'])
                    pass
                    # TODO: compare and Update path?
                else:
                    # print(start)
                    front_matter['path'] = slug
                    front_matter_string = yaml.dump(front_matter)
                    split_content[1] = front_matter_string
                    if "{" in front_matter_string:
                        print(front_matter_string)

                    joined_content = ("---\n").join(split_content)
                    # print(joined_content.split('---')[1])

