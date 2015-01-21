from fiona import collection


def read_txt(filename):
    """Read a text file and return a list of rows

    @param string filename: path to file to open
    @returns: list lines from text file
    """
    with open(filename, 'r') as lines:
        return lines.readlines()


def write_shape(filename, schema, data):
    """Write data to filename based on schema as ESRI shape format

    @param string filename: path to output file
    @param dict schema: data schema
    @param list data: list of dicts with data
    """
    with collection(filename, "w", "ESRI Shapefile", schema) as output:
        for row in data:
            output.write(row)
