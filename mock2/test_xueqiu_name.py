from mitmproxy import ctx, http
import mitmproxy.http


class Events:
    def response(self, flow: mitmproxy.http.HTTPFlow):
        if "https://stock.xueqiu.com/v5/stock/batch/quote.json?_t=" in flow.request.pretty_url and "x=" in flow.request.pretty_url:
            ctx.log.info("====================this is a response======================")
            with open(f"quote.json") as f:
                flow.response = http.HTTPResponse.make(
                    200,
                    f.read()
                )


addons = [
    Events()
]

if __name__ == "__main__":
    from mitmproxy.tools.main import mitmdump

    # 使用debug模式启动 mitmdump
    mitmdump(['-p', '8080', '-s', __file__])
