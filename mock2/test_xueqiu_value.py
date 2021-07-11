import json
from mitmproxy import ctx, http
import mitmproxy.http


class Events:
    def response(self, flow: mitmproxy.http.HTTPFlow):
        if "https://stock.xueqiu.com/v5/stock/batch/quote.json?_t=" in flow.request.pretty_url and "x=" in flow.request.pretty_url:
            ctx.log.info("===================this is a response======================")
            data = json.loads(flow.response.text)
            ctx.log.info("================this is a response data====================")
            ctx.log.info(str(data))
            for i in range(5):
                if i == 0:
                    data["data"]["items"][i]["quote"]["percent"] = "0"
                elif i == 1:
                    data["data"]["items"][i]["quote"]["percent"] = "-1"
                elif i == 2:
                    data["data"]["items"][i]["quote"]["percent"] = "1"
                elif i == 3:
                    data["data"]["items"][i]["quote"]["percent"] = "0.000000000000000001"
                elif i == 4:
                    data["data"]["items"][i]["quote"]["percent"] = "-0.000000000000000001"
            flow.response.text = json.dumps(data)


addons = [
    Events()
]

if __name__ == "__main__":
    from mitmproxy.tools.main import mitmdump

    # 使用debug模式启动 mitmdump
    mitmdump(['-p', '8080', '-s', __file__])
