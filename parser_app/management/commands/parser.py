import warnings
from datetime import datetime
from decimal import Decimal

from django.core.management.base import BaseCommand

from parser_app.models import Parser


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('input_file', type=str, help='Input file (e.g., A.uff)')
        parser.add_argument('--csv', type=str, help='Output CSV file')
        parser.add_argument('--sqlite', action='store_true', help='Output SQL (no argument needed)')

    def reset_flags(self): return False, False

    def process_line_30(self, values): return [values[1], values[2], values[3]]

    def handle(self, *args, **options):
        input_file = options.get('input_file', None)
        if input_file:

            output_ls = []
            parsed_30_ls = []

            with open(input_file, 'r') as reader:
                mpanCore = None
                serialNo = None
                for line in reader.readlines():

                    # splitting line into | delimited list i.e. `values`
                    values = line.split('|')
                    values.remove('\n') if '\n' in values else None

                    if len(parsed_30_ls) != 0 and (parsed_30_flag is True) and (values[0] in ['026', '028']):
                        # storing data into the list
                        output_ls.append(sorted(parsed_30_ls, key=lambda x: x[2]))
                        parsed_30_ls = []

                    if line.startswith('026|'):
                        if len(values) != 3:
                            warnings.warn(f'026| does has {len(values)} columns, but 3 were required')
                        else:
                            mpanCore = values[1]
                        parsed_30_flag = False

                    elif line.startswith('028|'):
                        if len(values) != 3:
                            warnings.warn(f'028| does has {len(values)} columns, but 3 were required')
                        else:
                            serialNo = values[1]
                        parsed_30_flag = False

                    elif line.startswith('030|') and mpanCore and serialNo:
                        parsed_30_flag = True
                        if len(values) != 8:
                            warnings.warn(f'030| does has {len(values)} columns, but 8 were required')
                        items = self.process_line_30(values)

                        # if there was any warning with the format, we will not add
                        if None not in items:
                            items.insert(0, mpanCore)
                            items.insert(1, serialNo)
                            parsed_30_ls.append(items)
                    else:
                        parsed_30_flag = False

                if (len(parsed_30_ls) != 0) and (parsed_30_flag is True):
                    # storing data into the list
                    output_ls.append(sorted(parsed_30_ls, key=lambda x: x[2]))

            final_ls = []
            for ls in output_ls:
                final_ls += ls

            if options.get('sqlite', False):
                for item in final_ls:
                    try:
                        reading_dt = datetime.strptime(item[3], '%Y%m%d%H%M%S')
                    except ValueError as e:
                        warnings.warn(f'{e}')
                        reading_dt = None
                    try:
                        reading_val = Decimal(item[4])
                    except ValueError as e:
                        warnings.warn(f'{e}')
                        reading_val = None

                    if (reading_val is not None) or (reading_dt is not None):
                        Parser.objects.create(
                            mpanCore=item[0],
                            serialNo=item[1],
                            unique_serial=item[2],
                            ReadingDt=reading_dt,
                            readingVal=reading_val,
                        )

            elif options.get('csv', False):
                output_csv_file = options['csv']

                columns = ['mpanCore, serialNo, readingDt, readingVal, fileName\n']
                for item in final_ls:
                    columns.append(f"{','.join(item)}\n")

                with open(output_csv_file, 'w+') as writer:
                    writer.writelines(columns)



