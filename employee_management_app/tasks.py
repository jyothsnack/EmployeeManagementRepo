import xlwt

from datetime import datetime, timedelta
from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger
from celery.task import Task

from employee_management_app.models import EmployeeTasks

logger = get_task_logger(__name__)

@periodic_task(run_every=(crontab(minute=0, hour=0, day_of_week='sun')),
               name="generate_weekly_report",
               ignore_result=True)
def generate_weekly_report():
        '''Function to download task details in xls'''

        wb = xlwt.Workbook(encoding='utf-8')

        #adding sheet
        ws = wb.add_sheet("sheet1")

        # Sheet header, first row
        row_num = 0

        font_style = xlwt.XFStyle()
        # font_style.alignment.wrap = 1
        # headers are bold
        font_style.font.bold = True

        #column header names, you can use your own headers here
        columns = ['Employee Name', 'Task', 'Time', 'Status', ]
        ws.col(0).width = len(columns[0]) * 367
        ws.col(1).width = 7 * len(columns[1]) * 367
        ws.col(2).width = 4 * len(columns[2]) * 367
        ws.col(3).width = 2 * len(columns[3]) * 367

        #write column headers in sheet
        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)
        # Sheet body, remaining rows
        font_style = xlwt.XFStyle()
        font_style.alignment.wrap = 1
        #get your data, from database or from a text file...
        last_date = datetime.now() - timedelta(weeks=1)
        data = EmployeeTasks.objects.filter(created_at__gte=last_date).order_by('-created_at')
        for my_row in data:
            row_num = row_num + 1
            ws.write(row_num, 0, my_row.employee.username, font_style)
            ws.write(row_num, 1, my_row.name, font_style)
            ws.write(row_num, 2, my_row.created_at.strftime('%Y-%m-%d %H:%M:%S'), font_style)
            ws.write(row_num, 3, my_row.get_status_display(), font_style)

        wb.save('reports/WeeklyTaskReport' + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '.xls')
        logger.info('Generated weekly report!')