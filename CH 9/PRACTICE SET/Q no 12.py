with open("CH 9/PRACTICE SET/old.txt") as f:
    content = f.read()

with open("CH 9/PRACTICE SET/renamed_by_py","w") as f:
    f.write(content)

import os
os.remove("CH 9/PRACTICE SET/old.txt")