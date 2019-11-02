import openpyxl
import pprint


def getExcelData(startRow, endRow):
    wb = openpyxl.load_workbook('test.xlsx')
    sheet = wb[('Sheet1')]
    data = {}
    for row in range(startRow, endRow):
        version = sheet['A' + str(row)].value
        startTime = sheet['B' + str(row)].value
        endTime = sheet['C' + str(row)].value
        eventName = sheet['D' + str(row)].value
        eventStatus = sheet['E' + str(row)].value

        data.setdefault('version', version)
        data.setdefault('start', startTime)
        data.setdefault('end', endTime)
        # event = {'eventName': eventName, 'eventStatus': eventStatus}
        # data.setdefault('event' + str(row - startRow), event)
        events = {eventName: eventStatus}
        data.setdefault('event' + str(row - startRow), events)
    pprint.pprint(data)
    return data
