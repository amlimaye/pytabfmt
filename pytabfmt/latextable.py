__all__ = ['LatexTable', ]

import sys
import io

class LatexTable():
    def __init__(self, columns, fmt_strings):
        self.rows = []
        self.column_titles = columns
        self.fmt_strings = fmt_strings


    def add_row(self, row):
        assert len(row) == len(self.column_titles)
        self.rows.append(row)


    def write_buffer(self, f):
        colspec = format_column_specification(self.column_titles)
        f.write('\\begin{tabular}{%s}\n' % colspec)

        header = format_header_string(self.column_titles)
        f.write(header)

        for idx, r in enumerate(self.rows):
            last_row = determine_last_row(idx, self.rows)
            fmtd = format_row(self.fmt_strings, r, last_row)
            f.write(fmtd)

        f.write('\\end{tabular}\n')


    def write(self, fname):
        with open(fname, 'w') as f:
            self.write_buffer(f)


    def print_out(self):
        self.write_buffer(sys.stdout)


    def __repr__(self):
        pipe = io.StringIO()
        self.write_buffer(pipe)
        contents = pipe.getvalue()
        pipe.close()
        return contents


def determine_last_row(idx, rows):
    return idx == (len(rows) - 1)


def format_column_specification(col_titles):
    column_specs = ['l' for _ in col_titles]
    colspec = '|'.join(column_specs)
    return colspec


def format_header_string(headers):
    header_strings = ['%s & ' % h for h in headers]
    headers_concat = ''.join(header_strings)
    final = headers_concat[:-2] + '\\\\ \\hline \n'

    return final


def format_row(fmts, entries, last_row=False):
    format_strings = []
    for idx, fs in enumerate(fmts):
        if idx == 0:
            format_strings.append('%s' % fs)
        else:
            format_strings.append('$%s$' % fs)

    formatted_entries = []
    for fs, entry in zip(format_strings, entries):
        # if there is a None, then include a dash in the table to signal that
        # data has been omitted
        if entry is None:
            formatted_entries.append('$-$ & ')
        else:
            formatted_entries.append(fs % entry + ' & ')

    joined = ''.join(formatted_entries)

    if not last_row:
        final = joined[:-2] + ' \\\\ \n'
    else:
        final = joined[:-2] + ' \n'

    return final
