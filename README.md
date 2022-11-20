# IBL bioinformatics wiki development

Source code of the documents are the `*.md` files located in `source/` dir.

For markdown syntax and special syntax for MyST (our markdown parser), please check:

[https://myst-parser.readthedocs.io/en/latest/intro.html](https://myst-parser.readthedocs.io/en/latest/intro.html)

After a page is added, please create link in the `{toctree}` section of `index.md` file.

The document will rebuild on pull requests.

To test on your own environment, install with pip:

`pip install sphinx myst-parser`

The project is not using these but may be better to add:

sphinxcontrib-mermaid