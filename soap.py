from suds.client import Client
from suds.sax.text import Raw
from io import BytesIO
from xml.etree.ElementTree import Element, SubElement, Comment, tostring
from xml.etree import ElementTree as ET


client = Client('https://services.rs.ge/WayBillService/WayBillService.asmx?WSDL',
                location='https://services.rs.ge/WayBillService/WayBillService.asmx')

su=":206322102"
sp="123456789"



GOOD_LIST = """
<GOODS>
        <ID>0</ID>
        <W_NAME>კიტრი</W_NAME>
        <UNIT_ID>1</UNIT_ID>
        <UNIT_TXT>ცალი</UNIT_TXT>
        <QUANTITY>10</QUANTITY>
        <PRICE>10</PRICE>
        <AMOUNT>100</AMOUNT>
        <BAR_CODE>1234</BAR_CODE>
        <A_ID>0</A_ID>
</GOODS>
"""

TYPE = "2"
BUYER_TIN = "12345678910"  # მყიდველის პირადი ნომერი
BUYER_NAME = "კლიენტის სახელი გვარი"  # მყიველის სახელი გვარი
START_ADDRESS = "თბილისი, "
END_ADDRESS = "თბილისი,"  # კლიენტის მისამართი
TRANSPORT_COAST = "5"
TRANSPORTER_TIN = "203836233"  # გადამზისავის საიდენტიფიკაციო
STATUS = "0"  # 0 შენახული, 1 აქტივირებული, 2 დასრულებული
TRAN_COST_PAYER = "1"  # 1 მყიდველი, 2 გამყიდველი
SELER_UN_ID = "731937"
TRANS_ID = "7"

xml_ = Raw("""
<WAYBILL>
    <GOODS_LIST>
    %s
    </GOODS_LIST>
<ID>0</ID>
<TYPE>%s</TYPE>
<BUYER_TIN>%s</BUYER_TIN>
<CHEK_BUYER_TIN>1</CHEK_BUYER_TIN>
<BUYER_NAME>%s</BUYER_NAME>
<START_ADDRESS>%s</START_ADDRESS>
<END_ADDRESS>%s</END_ADDRESS>
<DRIVER_TIN></DRIVER_TIN>
<CHEK_DRIVER_TIN>1</CHEK_DRIVER_TIN>
<DRIVER_NAME></DRIVER_NAME>
<TRANSPORT_COAST>%s</TRANSPORT_COAST>
<TRANSPORTER_TIN>%s</TRANSPORTER_TIN>
<RECEPTION_INFO/>
<RECEIVER_INFO/>
<DELIVERY_DATE/>
<STATUS>%s</STATUS>
<SELER_UN_ID>%s</SELER_UN_ID>
<PAR_ID></PAR_ID>
<CAR_NUMBER></CAR_NUMBER>
<BEGIN_DATE/>
<TRAN_COST_PAYER>%s</TRAN_COST_PAYER>
<TRANS_ID>%s</TRANS_ID>
<TRANS_TXT></TRANS_TXT>
<COMMENT></COMMENT>
</WAYBILL>
""" % (GOOD_LIST, TYPE, BUYER_TIN, BUYER_NAME,
       START_ADDRESS, END_ADDRESS,
       TRANSPORT_COAST, TRANSPORTER_TIN,
       STATUS, SELER_UN_ID,
       TRAN_COST_PAYER, TRANS_ID))

goods_count = [1]

ls = ["ID", "W_NAME", "UNIT_ID", "UNIT_TXT", "QUANTITY", "PRICE", "AMOUNT", "BAR_CODE", "A_ID"]


def sub_element_with_text(parent, tag, text):
    attrib = {}
    element = parent.makeelement(tag, attrib)
    parent.append(element)
    element.text = text
    return element


waybill = Element('WAYBILL')

_GOOD_LIST = SubElement(waybill, 'GOODS_LIST')

for good in goods_count:
    new = SubElement(_GOOD_LIST, 'GOODS')
    for item_name in ls:
        el = sub_element_with_text(new, item_name, '0')
        '''
        el = SubElement(new, '%s' % item_name)
        if item_name == "ID":
            el.text = '0'
        if item_name == "W_NAME":
            el.text = 'სახელი'
        if item_name == "UNIT_ID":
            el.text = '1'  # ერთეულის ID
        if item_name == "UNIT_TXT":
            el.text = 'ცალი'  # ერთეულის სახელი
        if item_name == "QUANTITY":
            el.text = '1'
        if item_name == "PRICE":
            el.text = '10'
        if item_name == "AMOUNT":
            el.text = '10'
        if item_name == "BAR_CODE":
            el.text = '100000'
        if item_name == "A_ID":
            el.text = '0'
        '''

_ID = SubElement(waybill, 'ID')
_ID.text = "0"
_TYPE = SubElement(waybill,'TYPE')
_TYPE.text = "2"
_BUYER_TIN = SubElement(waybill, 'BUYER_TIN')
_BUYER_TIN.text = BUYER_TIN
_CHEK_BUYER_TIN = SubElement(waybill, 'CHEK_BUYER_TIN')
_CHEK_BUYER_TIN.text = "1"
_BUYER_NAME = SubElement(waybill, 'BUYER_NAME')
_BUYER_NAME.text = BUYER_NAME
_START_ADDRESS = SubElement(waybill, 'START_ADDRESS')
_START_ADDRESS.text = START_ADDRESS
_END_ADDRESS = SubElement(waybill, 'END_ADDRESS')
_END_ADDRESS.text = END_ADDRESS
_DRIVER_TIN = SubElement(waybill, 'DRIVER_TIN')
_DRIVER_TIN.text = ""
_CHEK_DRIVER_TIN = SubElement(waybill, 'CHEK_DRIVER_TIN')
_CHEK_DRIVER_TIN.text = "1"
_DRIVER_NAME = SubElement(waybill, 'DRIVER_NAME')
_DRIVER_NAME.text = ""
_TRANSPORT_COAST = SubElement(waybill, 'TRANSPORT_COAST')
_TRANSPORT_COAST.text = TRANSPORT_COAST
_TRANSPORTER_TIN = SubElement(waybill, 'TRANSPORTER_TIN')
_TRANSPORTER_TIN.text = TRANSPORTER_TIN
_RECEPTION_INFO = SubElement(waybill, 'RECEPTION_INFO')
_RECEIVER_INFO = SubElement(waybill, 'RECEIVER_INFO')
_DELIVERY_DATE = SubElement(waybill, 'DELIVERY_DATE')
_STATUS = SubElement(waybill, 'STATUS')
_STATUS.text = "0"
_SELER_UN_ID = SubElement(waybill, 'SELER_UN_ID')
_SELER_UN_ID.text = SELER_UN_ID
_PAR_ID = SubElement(waybill, 'PAR_ID')
_CAR_NUMBER = SubElement(waybill, 'CAR_NUMBER')
_BEGIN_DATE = SubElement(waybill, 'BEGIN_DATE')
_BEGIN_DATE.text = ""
_TRAN_COST_PAYER = SubElement(waybill, 'TRAN_COST_PAYER')
_TRAN_COST_PAYER.text = TRAN_COST_PAYER
_TRANS_ID = SubElement(waybill, 'TRANS_ID')
_TRANS_ID.text = TRANS_ID
_TRANS_TXT = SubElement(waybill, 'TRANS_TXT')
_TRANS_TXT.text = ""
_COMMENT = SubElement(waybill, 'COMMENT')
_COMMENT.text = ""


way = ET.tostring(waybill, encoding='unicode')

xml = Raw("""%s""" % way)
print(xml)

save_waybill = client.service.save_waybill(su, sp, xml)


print(save_waybill)

#print(save_waybill.RESULT.STATUS)
#print(save_waybill.RESULT.ID)


#waybill_id = save_waybill.RESULT.ID

#send_waybill = client.service.send_waybill(su, sp, waybill_id) # აბრუნებს ზედნადების ნომერს

#print(send_waybill)
