import argparse

def add_connection_parameters(parser):
    ### Connection parameter
    parser.add_argument(
        "-b", "--broker", dest="host", help="Uri of the broker", required=True, type=str
    )
    parser.add_argument(
        "-p", "--port", dest="port", help="Port used", required=True, type=int
    )

    ### Company parameters
    parser.add_argument(
        "-c", "--company", dest="company_id", help="Company ID", required=True, type=str
    )
    parser.add_argument(
        "-u", "--username", dest="username", help="Username", required=True, type=str
    )
    parser.add_argument(
        "-pass", "--password", dest="password", help="Password", required=True, type=str
    )
    parser.add_argument(
        "-id",
        "--client-id",
        dest="id",
        help="Client id [between 0 and 9]",
        required=True,
        type=int,
    )

def add_read_parameters(parser):
    parser.add_argument(
        "-uid", "--uid", dest="uid", help="Device ID", required=True, type=str
    )
    parser.add_argument(
        "-fid", "--fid", dest="fid", help="File ID", required=True, type=int
    )
    parser.add_argument(
        "-field", "--field-name", dest="field", help="Field name", required=True, type=str
    )

def add_write_parameters(parser): 
    parser.add_argument(
    "-uid", "--uid", dest="uid", help="Device ID", required=True, type=str
    )
    parser.add_argument(
        "-fid", "--fid", dest="fid", help="File ID", required=True, type=int
    )
    parser.add_argument(
        "-field", "--field-name", dest="field", help="Field name", required=True, type=str
    )
    parser.add_argument(
        "-val", "--value", dest="value", help="Value", required=True, type=int
    )