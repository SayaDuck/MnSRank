from jinja2 import Environment, FileSystemLoader
import os

def generate(title,tournamentdata,playerdata,playerinfo):
    root = os.path.dirname(os.path.abspath(__file__))
    templates_dir = os.path.join(root, 'templates')
    env = Environment( loader = FileSystemLoader(templates_dir) )
    template = env.get_template('index.html')
    
    
    filename = os.path.join(root, 'index.html')
    with open(filename, 'w') as fh:
        fh.write(template.render(
            title = title,
            tourneylist = tournamentdata,
            playerlist = playerdata,
            playerinfo = playerinfo
        ))