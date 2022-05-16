# Developing the workshop

> ##### :warning: NOTE
> These steps are not necessary for the workshop. They exist here as documentation for the presenters.

All source files for this workshop live in this directory. It is a collection of jinja2 templates and some build scripts. You need to install the development dependencies by running `pip install -r  requirements.dev.txt`.

To build the tutorial run `make tutorial`. This step will compile `src/tutorial.md` to the parent directory and copy all the relevant python files.

To generate the fake dataset run `make data`. It generates the `2020VAERSLike.csv` file.

To run both, type `make all`.