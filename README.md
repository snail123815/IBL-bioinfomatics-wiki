# IBL bioinformatics wiki document co-authoring

Address:

https://ibl-bioinformatics-wiki.readthedocs.io/index.html

Source code of the documents are the `*.md` files located in `source/` dir.

For markdown syntax and special syntax for MyST (our markdown parser), please check:

https://myst-parser.readthedocs.io/en/latest/intro.html

## How to make changes

### Prerequisites

Clone this repository to your local machine. Make sure you have a python environment which has the following prerequisites (use pip install):

- sphinx
- myst-parser
- sphinx-copybutton
- sphinxcontrib-mermaid

Sphinx is a documentation generator that translates a set of plain text source files into output document. For us, is to translate markdown files to HTML files. Sphnix document can be found [here](https://www.sphinx-doc.org/en/master/usage/quickstart.html).

(Simply write `.md` file if you do not want to build and test.)

### General pipeline

Check [this page](https://www.freecodecamp.org/news/a-simple-git-guide-and-cheat-sheet-for-open-source-contributors/) for how to contribute. Here is a brief summary.

Genearly:

1. Fork this repository
2. Download your forked repository to your local machine. Or open a Codespace.
3. Create a branch of your own `git checkout -b your-branch-name`, do not touch "main" branch.
   1. Check your remote status
      `git remote -v`
      The result should contain two lines starts with `upstream https://github.com/snail123815/IBL-bioinformatics-wiki.git`
   2. Pull from upstream again to keep updated. You need to do this from time to time during your development (writing).
      `git pull upstream main`
   3. Work on your contributions. From time to time, you can summarise part of your work with `git add path/to/your.md` and commit it to your branch `git commit -m "your commit message"`, then push to your branch `git push --set-upstream origin your-branch-name` (`--set-upstream origin your-branch-name` only needs to be done the first time you push).
4. Once finished, pull from upstream main again to merge changes from upstream, then push all changes you made.
5. Go to the webpage of your forked repository, a green button "Compare & pull request" appear, click it, follow the screen to write messages. When I saw it, and checked everything is correct, I will approve the merge.

#### How to work on your contribution

Create a markdown `.md` file for your topic, write your content in markdown. Here is the [syntax](https://myst-parser.readthedocs.io/en/latest/intro.html). If you are writing tutorial, please make sure that every people you are targeting can understand, and test your tutorial well in all environments you can think of.

After a page is added, please do either:

1. If you are working on a topic belongs to one of the current major topics, put your file path (relative to `index.md`) in the `{toctree}` section as others.
2. If you are working on a complete new topic, create an additional `{toctree}` section in `index.md` file. Also, please put this in anywhere of your page (better in front):

   ````
   ```{toctree}
   ---
   #caption: Table of contents
   maxdepth: 3
   ---
   ```
   ````

You can now build the html page locally to see if your content is correctly formatted. Make sure you have installed [prerequisites](#prerequisites). Under `docs/` dir, run `make html`, then open `docs/build/html/index.html` to see the result.

Once you are satisfied, commit your changes to this branch. It is good to check now if the original repository has changed or not by `git pull upstream main`

Assume everything is alright now, you can push your branch, then create a pull request.

After pull request has been approved, the document will then rebuild and publish automatically.
