from PIL import Image
from PIL import ImageDraw, ImageFont

import xlwings as xw


# 获取表数据：

def get_img():
    visible_in = True
    # visible_in = True
    go_app = xw.App(visible=visible_in, add_book=False)
    print("数据入导...处理中...")
    wb_info = go_app.books.open('导入日期.xlsx')
    sht_info = wb_info.sheets[0]
    rag_info_max = sht_info.range(1, 1).expand().shape[0]

    # print("info最大行数：%s" % rag_info_max)
    # 获取帐号情况列表
    data_list = sht_info.range('A1' + ':F' + str(rag_info_max)).value[1:]
    print(data_list)

    for i, data in enumerate(data_list):
        im = Image.open('mode_001.jpg')
        draw = ImageDraw.Draw(im)
        fnt_1 = ImageFont.truetype(r'C:\Windows\Fonts\msyh.ttf', 50)
        fnt_2 = ImageFont.truetype(r'C:\Windows\Fonts\msyh.ttf', 40)
        fnt_3 = ImageFont.truetype(r'C:\Windows\Fonts\msyh.ttf', 85)
        fnt_4 = ImageFont.truetype(r'C:\Windows\Fonts\msyh.ttf', 30)
        fnt_5 = ImageFont.truetype(r'C:\Windows\Fonts\msyh.ttf', 30)

        cell_phone = str(data[0]).replace(".0", "")
        date_times = str(data[5])
        rx_times = str(data[3])
        tx_times = str(data[4])

        draw.text((155, 28), cell_phone, fill=(27, 27, 27), font=fnt_1)
        draw.text((428, 167), date_times, fill=(180, 180, 180), font=fnt_2)
        draw.text((277, 493), cell_phone, fill=(59, 149, 233), font=fnt_3)
        draw.text((848, 1369), rx_times, fill=(143, 167, 138), font=fnt_4)
        draw.text((172, 1581), tx_times, fill=(146, 146, 146), font=fnt_5)
        # im.show()
        im.save(str(i) + '_' + cell_phone + '.jpg')


get_img()
