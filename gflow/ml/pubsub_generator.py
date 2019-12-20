import time
import argparse

import pandas as pd

from google.cloud import pubsub_v1


def generate_text(path):
    """Create new messages for pubsub based on a ticket_message dataset.

    :arg path: (str) dataset path
    :return: (generator) generator of messages
    """
    df = pd.read_csv(path)
    for idx, row in df.iterrows():
        yield row['stripped_text']


def callback(message_future):
    """Callback in case of fail.

    :arg message_future: (publisher.futures) the new message to push
    """
    if message_future.exception(timeout=30):
        print('Publishing message threw an Exception {}.'.format(message_future.exception()))
    else:
        print(message_future.result())


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
        '--dataset-path',
        required=True,
        help="Dataset path to push new messages to pubsub")

    args, pipeline_args = parser.parse_known_args()
    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(args.project_id, args.input_topic)
    line = generate_text(args.dataset_path)
    while True:
        time.sleep(0.33)
        message_future = publisher.publish(topic_path, data=line.next())
        message_future.add_done_callback(callback)
