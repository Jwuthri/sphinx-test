.. gorgias-dataflow documentation master file, created by
   sphinx-quickstart on Wed Dec 18 17:35:01 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to gorgias-dataflow's documentation!
============================================

.. toctree::
   :maxdepth: 2

   gflow

Getting Started
================

Prepare your environment

.. toctree::
   :maxdepth: 4

   install.rst

This package require python 2.7 sorry boys :(

*For your local needs*, you can create a virtualenv::

    python2.7 -m virtualenv gdataflow
    source gdataflow/bin/activate
    pip install beam==0.5.0

Or use conda::

    conda create -n gdataflow python=2.7
    conda activate gdataflow
    pip install beam==0.5.0



Running Workflow
----------------

.. toctree::
   :maxdepth: 4

   runworkflow.rst

::

   gcloud auth application-default login

   pip install .

Environment Variables
~~~~~~~~~~~~~~~~~~~~~

Before running the workflow on DataFlow you must set the correct
``PROJECT`` and ``BUCKET`` and ``INPUT_TOPIC`` and ``OUTPUT_TOPIC``
environment variables to be used to execute the pipeline.

For example:

::

   PROJECT=gorgias-ml-development
   BUCKET=gs://gorgias-ml-development-data
   INPUT_TOPIC=ml-input
   OUTPUT_TOPIC=ml-output
   BIGQUERY=ticket_messages.summarization_table

Create the pubsub topics if it’s not already done:

::

   # To create the inputs topic
   gcloud pubsub topics create ml-input

   # To create the outputs topic
   gcloud pubsub topics create ml-output

To delete the topics:

::

   # To create the inputs topic
   gcloud pubsub topics delete ml-input

   # To create the outputs topic
   gcloud pubsub topics delete ml-output

First step (terminal 1)
~~~~~~~~~~~~~~~~~~~~~~~

You need to push new data to your topic (in reality, data will come from
the helpdesk)

::

   python gflow/ml/pubsub_generator.py \
     --project-id $PROJECT \
     --input-topic $INPUT_TOPIC \
     --dataset-path data/pubsub_generator_dataset.csv

   You can find the csv file here: gorgias-ml-development-data/gorgias-dataflow/data

Second step (terminal 2)
~~~~~~~~~~~~~~~~~~~~~~~~

You need to read the data from the topic and apply your algorithms on

::

   # Local
   python gflow/ml/subscriber.py \
     --project-id $PROJECT \
     --input-topic $INPUT_TOPIC \
     --output-topic $OUTPUT_TOPIC \
     --runner DirectRunner \
     --project $PROJECT \
     --streaming

   # Cloud
   python gflow/ml/subscriber.py \
     --job_name gorgias-dataflow-subscriber-$PROJECT \
     --project-id $PROJECT \
     --input-topic $INPUT_TOPIC \
     --output-topic $OUTPUT_TOPIC \
     --runner DataflowRunner \
     --project $PROJECT \
     --staging_location $BUCKET/gorgias-dataflow/staging \
     --temp_location $BUCKET/gorgias-dataflow/temp \
     --streaming

Last one (terminal 3)
~~~~~~~~~~~~~~~~~~~~~

You need to read data from output topic and push them into BigQuery

::

   # Local
   python gflow/ml/publisher.py \
     --project-id $PROJECT \
     --input-topic $OUTPUT_TOPIC \
     --output ./tmp/gorgias-dataflow \
     --bigquery-table $BIGQUERY \
     --runner DirectRunner \
     --project $PROJECT \
     --streaming

   # Cloud
   python gflow/ml/publisher.py \
     --job_name gorgias-dataflow-publisher-$PROJECT \
     --project-id $PROJECT \
     --input-topic $OUTPUT_TOPIC \
     --bigquery-table $BIGQUERY \
     --runner DataflowRunner \
     --project $PROJECT \
     --staging_location $BUCKET/gorgias-dataflow/staging \
     --temp_location $BUCKET/gorgias-dataflow/temp \
     --streaming

You should see 2 news dataflow’ job, and query the bigquery table to
check the number of rows

Ticket format
=============

You can have an example of ticket, with all the keys and additional information

.. toctree::
   :maxdepth: 4

   ticketformat.rst

Module Index
============

Here you can check all the modules following the code architecture, and go deeper in the code

.. toctree::
   :maxdepth: 4

   moduleindex.rst

Index
=====

Here you can check all the functions alphabetical order

.. toctree::
   :maxdepth: 4

   generateindex.rst

Prices
======

Here is a summary report for dataflow

.. toctree::
   :maxdepth: 4

   prices.rst
