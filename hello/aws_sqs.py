from boto.sqs.message import MHMessage
import boto.sqs
from boto.compat import StringIO

REGION = 'us-west-2'

PICTURES = 'pictures'


def sendMessage(design):
    connection = boto.sqs.connect_to_region(REGION)

    boto.sqs.connect_to_region('us-west-2')

    queue = connection.get_queue(PICTURES)

    data = {
        'id': design.pk,
        'designer_id': design.designer.pk,
        'project_id': design.project.pk,
        'image_url': design.imageFile.url
    }

    message = MHMessage(body=data)

    queue.write(message)


def getMessages():

    connection = boto.sqs.connect_to_region(REGION)

    queue = connection.get_queue(PICTURES)

    messages = queue.get_messages()

    results = []

    for m in messages:
        msg = decode_message(m.get_body())
        results.append(msg)

    print results

    if results[0]:
        print results[0].get('id')
        print results[0].get('designer_id')
        print results[0].get('project_id')
        print results[0].get('image_url')


    return results


def decode_message(body):
    try:
        msg = {}
        fp = StringIO(body)
        line = fp.readline()
        while line:
            delim = line.find(':')
            key = line[0:delim]
            value = line[delim+1:].strip()
            msg[key.strip()] = value.strip()
            line = fp.readline()
    except:
        print 'error'

    return msg
