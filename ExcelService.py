import openpyxl
import pprint


def getExcelData(startRow, endRow):
    wb = openpyxl.load_workbook('test.xlsx')
    sheet = wb[('Sheet1')]
    data = {}
    events = []
    todos = []
    # 看能不能把参数去掉
    # i = 0
    # for cell in sheet["A"]:
    #     if cell.value is not None:
    #         i += 1
    for row in range(startRow, endRow + 1):
        # 将datetime转换为字符串 去掉时分秒
        startTime = str(sheet['A' + str(row)].value).replace("00:00:00", "").strip()
        endTime = str(sheet['B' + str(row)].value).replace("00:00:00", "").strip()

        version = sheet['D' + str(row)].value
        eventName = sheet['E' + str(row)].value
        eventStatus = sheet['G' + str(row)].value
        todoEvent = sheet['H' + str(row)].value

        data.setdefault('version', version)
        data.setdefault('start', startTime)
        data.setdefault('end', endTime)

        events.append({"eventName": eventName, "eventStatus": eventStatus})
        if todoEvent is not None:
            todos.append({"todoName": todoEvent})

    data.setdefault('events', events)
    data.setdefault('todos', todos)
    pprint.pprint(data)
    return data
