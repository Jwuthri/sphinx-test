gorgias-dataflow
=============================

[![Python 2.7](https://img.shields.io/badge/python-2.7-blue.svg)](https://www.python.org/downloads/release/python-270/)

Build dataflow pipeline for Gorgias project

## Running Workflow

### Environment Variables

Before running the workflow on DataFlow you must set the correct `PROJECT` and `BUCKET` environment variables to be used to execute the pipeline.

For example:

    PROJECT=your-project-id  # $(gcloud config get-value project)
    BUCKET=your-bucket-name

    gcloud auth application-default login

### Locally

    python gorgias-dataflow_main.py \
      --job_name gorgias-dataflow-$PROJECT \
      --project $PROJECT \
      --runner DirectRunner \
      --output ./tmp/gorgias-dataflow

### Google Cloud DataFlow

    python gorgias-dataflow_main.py \
      --job_name gorgias-dataflow-$PROJECT \
      --project $PROJECT \
      --runner DataflowRunner \
      --setup_file ./setup.py \
      --staging_location gs://$BUCKET/gorgias-dataflow/staging \
      --temp_location gs://$BUCKET/gorgias-dataflow/temp \
      --output gs://$BUCKET/gorgias-dataflow/gorgias-dataflow


### Generate the doc

    pip install .
    cd docs
    sphinx-apidoc -o source/ ../gflow
    make html
    
    open the file in docs/_build/index.html