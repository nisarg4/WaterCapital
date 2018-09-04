from os.path import isfile

import xlrd
import logging

from firstapp.models import Transactio

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
filepath = "/home/flame/Desktop/test.xls"

if isfile(filepath):
    data_reader = csv.reader(open(filepath, 'rb'), delimiter='|')
    logger.info("importing to %s" % Transactio)
    # vaciar la tabla
    Transactio.objects.all().delete()

    if type(formatter) == list:
        format = lambda d: dict(zip(formatter, d))
    else:
        format = formatter
    i = 0
    for row_value_list in data_reader:
        data = format(row_value_list)
        if data:
            obj = Transactio(**data)
            obj.save()
            i = i + 1
        else:
            logger.error("incomplete data %s" % data)

    logger.info("%s objects imported to %s" % (i, Transactio))
else:
    logger.error("temp import file not found")


def import_xls_to_db(filepath, model, model_mapping):
    """ Imports data from .xls to db"""
    first_row = 1

    if isfile(filepath):
        book = xlrd.open_workbook(filepath, encoding_override='cp1252')
        sheet = book.sheet_by_index(0)
        nr_rows = sheet.nrows
        for row in range(first_row, nr_rows):
            """row_value_list = []
            for cell in sheet.row(row):
                if cell.ctype == 3:
                    date_tuple = xlrd.xldate_as_tuple(cell.value, book.datemode)
                    cell_value = "%s-%s-%s" % date_tuple
                else:
                    cell_value = cell.value"""
            row_value_list = [cell.value for cell in sheet.row(row)]
            if (type(model_mapping) == dict):
                da = zip(model_mapping.keys(), row_value_list)
                data = dict([(i[0], model_mapping[i[0]](i[1])) for i in da])
            else:
                data = dict(zip(model_mapping, row_value_list))
            print
            data
            obj = model(**data)
            obj.save()
            msg = "imported %s" % data
            logger.info(msg)