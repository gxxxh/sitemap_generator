import os
from source.parsegitpage import ParseGitPage
from source.config import *
# html字符串





if __name__ == "__main__":
    dir = os.path.join(WORKPATH, "TVMChinese")
    parser = ParseGitPage(dir=dir,html=HTMLSUFFIX,root_url=ROOTURL)
    parser.add_homepage()
    pt = parser.parse_dir("")
    parser.save("TVMChinese.xml")