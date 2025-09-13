# DSPy extraction data pipeline for assisted prompt enhancing

The structure of this project follows the convention of [🍪📊
cookiecutter-datascience](https://cookiecutter-data-science.drivendata.org/#directory-structure)
with those specificities:

- the python package with the source code to be run locally on the notebooks or
in the experimental scripts is in a **poetry project**, defined in the `src`
subdirectory
- most of the code in the [`./models/`](./models/) subdirectory is there to
serve remote models reachable through HTTP connections

## Set the environment

Please visit the [Installation section of the
documentation](https://magoh-ai-docs.mappa.cloud.thormas.fr/install/).

## Try some experiments

The
[`3.0-Convolutio-complete_pipeline.ipynb`](./notebooks/exploratory/3.0-Convolutio-complete_pipeline.ipynb)
notebook contains the most straight-forward code to demonstrate the last
features of this project, including:

- inferring in the most complex model with a set of archaeological excavation
reports
- optimizing this model
- evaluating it and plotting its scores

To set your custom experiments and create other models (e.g. with just
different hyperparameters, etc.), please read [the *How-to guides in the
documentation*](https://magoh-ai-docs.mappa.cloud.thormas.fr/how-to-guides/).
