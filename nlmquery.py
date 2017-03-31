import argparse
import sys
from os.path import basename
from PyZ3950 import zoom


def parse_args(argv):
    parser = argparse.ArgumentParser(prog = basename(__file__))
    parser.add_argument('nlmui', nargs='+', type=int, help='Give an NLM UI to query')
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


def search(conn, nlmui):
    query = zoom.Query('PQF', '@attr 1=1062 %s' % str(nlmui))
    res = conn.search(query)
    for r in res:
        print(str(r))
    print('\n')


def main(argv):
    opts = parse_args(argv)
    conn = open_connection(opts)

    for nlmui in opts.nlmui:
        search(conn, nlmui)


if __name__ == '__main__':
    main(sys.argv)

