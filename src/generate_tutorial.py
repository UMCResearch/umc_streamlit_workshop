from pathlib import Path
from jinja2 import Environment, FileSystemLoader

tutorial_src_file = Path("tutorial.md")

tutorial_src_dir = tutorial_src_file.parent.absolute()

env = Environment(
    loader=FileSystemLoader([
        tutorial_src_dir, 
        tutorial_src_dir.parent
    ]),
    keep_trailing_newline=True
)

template = env.get_template(tutorial_src_file.name)

Path(tutorial_src_dir.parent / tutorial_src_file.name).write_text(template.render())