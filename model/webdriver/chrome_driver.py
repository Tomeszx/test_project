from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


class Driver(webdriver.Chrome):
    def __init__(self):
        options = self._get_browser_options()
        super().__init__(service=Service(), options=options)
        self.set_page_load_timeout(20)
        send_command = ('POST', f'/session/{self.session_id}/chromium/send_command')
        self.command_executor._commands[f'SEND_COMMAND_{self.session_id}'] = send_command

    @classmethod
    def _get_browser_options(cls) -> Options:
        options = Options()
        options.add_argument("--enable-automation")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-browser-side-navigation")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")
        options.page_load_strategy = "eager"
        return options
