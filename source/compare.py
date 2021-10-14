from source.parsegitpage import ParseGitPage


def compare(old_dir, new_dir,html,root_url):
    xml = ParseGitPage(dir=old_dir,html=html,root_url=root_url)
    xml.add_homepage()
    pt = xml.parse_dir("")
    #pass
