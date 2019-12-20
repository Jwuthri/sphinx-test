import json
import argparse

import apache_beam as beam


class DbFormat(beam.DoFn):
    """Transform a prediction into a BigQuery format."""

    def to_runner_api_parameter(self, unused_context):
        pass

    def process(self, element):
        """just format the output of summarization for BigQuery.

        :param element: (json) prediction in json format
        :return: (list) new raw to insert
        """
        return [
            {
                "tags_positions": str(element['tags_positions']),
                "mode": element['mode'],
                "prediction": element['prediction']
            }
        ]


def run(args, pipeline_args):
    """Run the dataflow job, locally or on the cloud

    :param args: (argparse.Namespace) all the command line args
    :param pipeline_args: (list) all the command line pipeline args
    """
    schema = "tags_positions: STRING, mode: STRING, prediction: STRING"
    topic_input_path = "projects/{}/topics/{}".format(args.project_id, args.input_topic)
    p = beam.Pipeline(options=beam.options.pipeline_options.PipelineOptions())
    (p
      | 'ReadData' >> beam.io.ReadFromPubSub(topic=topic_input_path)
      | "FilterNone" >> beam.Filter(lambda x: x is not None)
      | 'Jsonify' >> beam.Map(json.loads)
      | 'DatabaseFormatting' >> beam.ParDo(DbFormat())
      | 'WriteToBigQuery' >> beam.io.WriteToBigQuery(
            "{}:{}".format(args.project_id, args.bigquery_table),
            schema=schema, write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND))
    result = p.run()
    result.wait_until_finish()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument(
        '--project-id',
        required=True,
        help="Your gcp' project id, => $(gcloud config get-value project)")
    parser.add_argument(
        '--input-topic',
        required=True,
        help="Your topic input, => 'ml_input'")
    parser.add_argument(
        '--bigquery-table',
        required=True,
        help="The table of your bigquery")
    args, pipeline_args = parser.parse_known_args()

    run(args, pipeline_args)
