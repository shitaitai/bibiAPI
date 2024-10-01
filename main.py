from pkg.plugin.context import register, handler, llm_func, BasePlugin, APIHost, EventContext
from pkg.plugin.events import *  # 导入事件类


# 注册插件
@register(name="课代表插件", description="能够让机器人总结BILIBILI视频或者其他视频内容", version="0.1", author="师太太")
class WebwlkrPlugin(Plugin):

    def __init__(self, plugin_host: PluginHost):
        self.cfg: dict = None
        
        # 检查webwlkr.yaml是否存在
        if not os.path.exists("webwlkr.yaml"):
            shutil.copyfile("plugins/WebwlkrPlugin/config-template.yaml", "webwlkr.yaml")
        
        # 读取配置文件
        with open("webwlkr.yaml", "r", encoding="utf-8") as f:
            self.cfg = yaml.load(f, Loader=yaml.FullLoader)

    @func("access_the_web")
    def access_the_web(self, url: str, brief_len: int) -> str:
        """Call this function to access the specified API and retrieve content.
        
        Args:
            url (str): URL to visit (not used in this implementation).
            brief_len (int): Max length of the plain text content.

        Returns:
            str: Plain text content from the API response or error message (starts with 'error:').
        """
        api_url = "https://bibigpt.co/api/open/yRvg40M7C4cn"
        
        try:
            # 发送 GET 请求到 API
            response = requests.get(api_url)
            response.raise_for_status()  # 如果响应状态码不是 200，将引发异常
            
            data = response.json()  # 将响应内容解析为 JSON 格式
            
            # 假设返回的数据中有一个 'content' 字段，您可以根据实际情况调整
            content = data.get('content', '')
            
            if len(content) > brief_len:
                return content[:brief_len]  # 限制返回长度
            
            return content  # 返回完整内容

        except Exception as e:
            logging.error("[Webwlkr] error accessing API: {}".format(e))
            return "error accessing API: {}".format(e)
