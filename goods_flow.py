GOOD_FLOW_API_URL = "https://ws1.goodsflow.com/GWS/api/Member/v3/TraceInfoByUniqueCode/trenbe/RESALE_IA_RETURN_UC_%s"
CONTENT_TYPE = "application/json;charset=utf-8"
GOODS_FLOW_API_KEY = "[Replace by Goodflow API Key]"

HEADERS = {
    'Content-Type': CONTENT_TYPE,
    'goodsFLOW-Api-Key': GOODS_FLOW_API_KEY
}

# Req/Res Const
CJ_CLS = 'CJGLS'
UNPICKED = 'UNPICKED'
UNKNOWN = 'UNKNOWN'
UNKNOWN_DESC = '알 수 없음'
LAST_DELIVERY_STAT_TYPE_KEY = 'lastDlvStatType'
INVOICE_NO = 'invoiceNo'
LOGISTICS_CODE = 'logisticsCode'
LAST_DLV_STAT_NAME = 'lastDlvStatName'
GOODS_FLOW_DATA_KEY = 'data'

# Goodsflow Input
GOODS_FLOW_TARGET_FILENAME = 'resources/input/delivery_ids.txt'

# Goodsflow Output
GOODS_FLOW_RES_FILENAME = 'resources/output/delivery_info_output.txt'

