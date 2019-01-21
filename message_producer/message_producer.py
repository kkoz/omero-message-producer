#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# registration_server - CellLibrarian Registration Server
#
# Copyright (c) 2017 Glencoe Software, Inc.  All rights reserved.
#
# This software is distributed under the terms described by the LICENCE.txt
# file you can find at the root of the distribution bundle.  If the file is
# missing please request a copy by contacting info@glencoesoftware.com.

import sys
import pika
import json
import logging
import click

from configobj import ConfigObj

import pdb

logging.basicConfig()
log = logging.getLogger('omero-message-producer')
log.setLevel("INFO")

@click.command()
@click.argument('config')
@click.argument('srcpath')
def send_message(config, srcpath):
    config = ConfigObj(config, interpolation=False)
    queue_url = config['server.rabbitmq.url']
    parameters = pika.connection.URLParameters(queue_url)
    body_data = {'filepath' : srcpath}
    log.info(json.dumps(body_data))
    queue_name = config['server.rabbitmq.message_queue']
    log.info("Sending filepath %s to queue %s" % (srcpath, queue_name))
    with pika.BlockingConnection(parameters) as conn:
        channel = conn.channel()
        channel.basic_publish(exchange='',
                              routing_key=queue_name,
                              body=json.dumps(body_data))
        log.info("Sent message")

