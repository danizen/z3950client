#!/usr/bin/env python2
import argparse
import sys
from os.path import basename
from PyZ3950 import zoom


def parse_args(argv):
    parser = argparse.ArgumentParser(prog = basename(__file__))
    parser.add_argument('identifier', nargs='+', help='Give an NLM UI to query')
    parser.add_argument('--type', metavar='IDTYPE',
                        choices=['query', 'nlmui', 'mmsid', 'issn', 'isbn'],
                        default='nlmui')
    parser.add_argument('--host', metavar='HOSTNAME', default='ilsz3950.nlm.nih.gov')
    parser.add_argument('--port', metavar='PORT', default='7091')
    parser.add_argument('--database', metavar='NAME', default='VOYAGER')
    parser.add_argument('--syntax', metavar='SYNTAX', default='USMARC',
                        help='The preferred record syntax')

    return parser.parse_args(argv[1:])


def open_connection(opts):
    conn = zoom.Connection(opts.host, int(opts.port))
    conn.databaseName = opts.database
    conn.preferredRecordSyntax = opts.syntax
    return conn


def search(conn, query_type, identifier):
    query_string = None
    if query_type == 'nlmui':
        query_string = '@attr 1=1062 @attr 2=3 "%s"' % str(identifier)
    elif query_type == 'issn':
        query_string = '@attr 1=8 @attr 2=3 "%s"' % str(identifier)
    elif query_type == 'isbn':
        query_string = '@attr 1=7 @attr 2=3 "%s"' % str(identifier)
    elif query_type == 'query':
        query_string = identifier
    else:
        query_string = '@attr 1=12 @attr 2=3 "%s"' % str(identifier)
    query = zoom.Query('PQF', query_string)
    res = conn.search(query)
    for r in res:
        print(str(r))
    print('\n')


def main(argv):
    opts = parse_args(argv)
    conn = open_connection(opts)

    for identifier in opts.identifier:
        search(conn, opts.type, identifier)


if __name__ == '__main__':
    main(sys.argv)

