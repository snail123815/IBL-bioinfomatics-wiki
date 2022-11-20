# IBL bioinformatics wiki document co-authoring

Address:

[https://ibl-bioinfomatics-wiki.readthedocs.io/index.html](https://ibl-bioinfomatics-wiki.readthedocs.io/index.html)

Source code of the documents are the `*.md` files located in `source/` dir.

For markdown syntax and special syntax for MyST (our markdown parser), please check:

[https://myst-parser.readthedocs.io/en/latest/intro.html](https://myst-parser.readthedocs.io/en/latest/intro.html)

After a page is added, please create link in the `{toctree}` section of `index.md` file.

## How to make changes

### Prerequisites

Clone this repository to your local machine. Make sure you have a python environment which has the following prerequisites:

- sphinx
- myst-parser
- sphinxcontrib-mermaid (not yet used)

Sphinx is a documentation generator that translates a set of plain text source files into output document. For us, is to translate markdown files to HTML files. Sphnix document can be found [here](https://www.sphinx-doc.org/en/master/usage/quickstart.html).

(Simply write `.md` file if you do not want to build and test.)

### General pipeline

In issues, make a new issue explaining what you want to do. If it is simple, just a short title like "complete intro" would be enough. Assign this issue to yourself, submit this issue.

At the right side of the issue you created, you will find "Development" section, "create a branch" for this issue and checkout locally.

After making changes to source code (`.md` files), enter `/docs` dir and run `make html`, then open `/docs/build/html/index.html` to see the result.

Once it is satisfied, commit your changes to this branch, then create a pull request (Code -> branches -> "New pull request" from the branch you are working on). One other people needs to approve this and merge (please do "squash and merge") to `main` branch.

The document will then rebuild and publish automatically.