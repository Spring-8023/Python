# -*- coding:utf-8 -*-
import xlwt
import xlrd
import json
# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')
import os
cur_path = os.path.dirname(__file__)
file = cur_path + '/Data/test.xls'


# 设置表格样式
def set_style(name, height, bold=False):
    style = xlwt.XFStyle()
    font = xlwt.Font()
    font.name = name
    font.bold = bold
    font.color_index = 4
    font.height = height
    style.font = font
    return style

# 写Excle
def write_excel():
    f = xlwt.Workbook(encoding='utf-8')
    sheet1 = f.add_sheet('学生', cell_overwrite_ok=True)
    row0 = ["姓名", "年龄", "出生日期", "爱好"]
    colum0 = ["张三", "李四2", "联系python", "小明", "小红", "无名", "小蓝"]
    # 写第一行
    for i in range(0, len(row0)):
        sheet1.write(0, i, row0[i], set_style('Time New Roman', 220, True))

    # 写第一列
    for i in range(0, len(colum0)):
        sheet1.write(i+1, 0, colum0[i], set_style('Time New Roman', 220, True))

    sheet1.write(1, 3, '2006/12/12')
    sheet1.write(2, 3, '2016/01/02')
    # sheet1.write_merge(6, 6, 1, 3, '未知')  # 合并单元格
    # sheet1.write_merge(1, 2, 3, 4, '打游戏')  # 合并列单元格
    # sheet1.write_merge(4, 6, 3, 3, '打篮球' )
    f.save('test.xls')

def read_excel():
    wb = xlrd.open_workbook(filename=file)  # 打开文件
    print(json.dumps(wb.sheet_names(), ensure_ascii=False))  # 获取所有表格名字
    sheet1 = wb.sheet_by_index(0)  # 通过索引获取表格
    sheet2 = wb.sheet_by_name(u'学生')  # 通过名字获取表格
    print(sheet1, sheet2)
    title = sheet1.row_values(0)
    print title
    data = []
    for i in range(1, sheet1.nrows):
        data.append(dict(zip(title, sheet1.row_values(i))))
    # print data
    print(json.dumps(data, ensure_ascii=False))



    # rows = sheet1.row_values(2)  # 获取行内容
    # cols = sheet1.col_values(3)  # 获取列内容
    # print(json.dumps(rows, ensure_ascii=False))
    # print(json.dumps(cols, ensure_ascii=False))



if __name__ == '__main__':
    # write_excel()
    read_excel()