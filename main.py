import time
import requests
import goods_flow


def query_to_goodsflow(delivery_id):
    print(f'Req = {goods_flow.GOOD_FLOW_API_URL % delivery_id}')
    res = requests.get(url=goods_flow.GOOD_FLOW_API_URL % delivery_id, headers=goods_flow.HEADERS)
    return res.json()


if __name__ == '__main__':
    with open(goods_flow.GOODS_FLOW_RES_FILENAME, 'a+') as wp:
        with open(goods_flow.GOODS_FLOW_TARGET_FILENAME, 'r') as rp:
            for delivery_id in rp:
                req_delivery_id = delivery_id.strip()
                res_json = query_to_goodsflow(delivery_id=req_delivery_id)
                res_data = res_json.get(goods_flow.GOODS_FLOW_DATA_KEY)
                if res_data is None:
                    log_line = '%s, -, -, %s, %s\n' % (req_delivery_id.strip(), goods_flow.UNKNOWN, goods_flow.UNKNOWN_DESC)
                    print(log_line)
                    wp.write(log_line)
                else:
                    logisticsCode = res_data.get(goods_flow.LOGISTICS_CODE)
                    invoiceNo = res_data.get(goods_flow.INVOICE_NO)
                    lastDlvStatType = res_data.get(goods_flow.LAST_DELIVERY_STAT_TYPE_KEY)
                    lastDlvStatName = res_data.get(goods_flow.LAST_DLV_STAT_NAME)
                    log_line = '%s, %s, %s, %s, %s\n' % (req_delivery_id, logisticsCode, invoiceNo, lastDlvStatType, lastDlvStatName)
                    print(log_line)
                    wp.write(log_line)
                time.sleep(0.5)
