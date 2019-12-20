import json
import argparse

import apache_beam as beam


def fake_summarization(data):
    """Produce 'fake' result for summarization (just as example).

    :param data: (str) ticket_message
    :return: (dict) summarization prediction
    """
    return {"tags_positions": [[1, 10]], "mode": "ranked", "prediction": data}


def run(args, pipeline_args):
    """Run the dataflow job, locally or on the cloud

    :param args: (argparse.Namespace) all the command line args
    :param pipeline_args: (list) all the command line pipeline args
    """
    topic_input_path = "projects/{}/topics/{}".format(args.project_id, args.input_topic)
    topic_output_path = "projects/{}/topics/{}".format(args.project_id, args.output_topic)
    p = beam.Pipeline(options=beam.options.pipeline_options.PipelineOptions())
    (p
      | 'ReadData' >> beam.io.ReadFromPubSub(topic=topic_input_path).with_output_types(bytes)
      | "Decode" >> beam.Map(lambda x: x.decode('utf-8'))
      | "FilterNone" >> beam.Filter(lambda x: x is not None)
      | "SummarizeText" >> beam.Map(fake_summarization)
      | 'FormatText' >> beam.Map(json.dumps)
      | "Write" >> beam.io.WriteToPubSub(topic=topic_output_path).with_output_types(bytes))
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
        '--output-topic',
        required=True,
        help="Your topic output, => 'ml_output'")
    args, pipeline_args = parser.parse_known_args()

    run(args, pipeline_args)
