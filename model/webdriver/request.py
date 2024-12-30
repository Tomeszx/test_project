import json
from logging import Logger

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.devtools.v119.network import ResourceType

from metrics.metrics import Metrics


class EmptyRequest:
    def __init__(self):
        self.request_id = None
        self.type = None
        self.url = None
        self.document_url = None
        self.method = None
        self.request_headers = None
        self.timestamp = 0
        self.payload = None
        self.response = None

    def to_dict(self) -> dict:
        data = self.__dict__.copy()
        data['response'] = self.response.__dict__
        return data


class Request:
    def __init__(self, request: dict):
        self.request_id = str(request['requestId'])
        self.type = str(request['type'])
        self.url = str(request['request']['url'])
        self.document_url = str(request['documentURL'])
        self.method = str(request['request']['method'])
        self.request_headers = request['request']['headers']
        self.timestamp = round(float(request['timestamp']), 2)
        self.payload = None
        self.response = None

    def __eq__(self, request_id: str) -> bool:
        return self.request_id == request_id

    def get_payload(self, driver: WebDriver) -> str | None:
        try:
            return driver.execute_cdp_cmd('Network.getRequestPostData', {"requestId": self.request_id})['postData']
        except Exception:
            return None

    def to_dict(self) -> dict:
        data = self.__dict__.copy()
        if self.response:
            data['response'] = self.response.__dict__
        return data


class Response:
    def __init__(self, response: dict):
        self.request_id = str(response['requestId'])
        self.type = str(response['type'])
        self.mime_type = response['response']['mimeType']
        self.remote_ip_address = response['response'].get('remoteIPAddress')
        self.remote_port = response['response'].get('remotePort')
        self.url = str(response['response']['url'])
        self.status = int(response['response']['status'])
        self.status_text = str(response['response']['statusText'])
        self.response_headers = response['response']['headers']
        self.response_time = float(response['response'].get('responseTime', 0))
        if 'timing' in response['response']:
            self.request_time = float(response['response']['timing'].get('requestTime', 0))
            self.receive_headers_end = float(response['response']['timing'].get('receiveHeadersEnd', 0))
        else:
            self.request_time = 0
            self.receive_headers_end = 0
        self.timestamp = round(float(response['timestamp']), 2)
        self.body = None
        self.has_error = False

    def get_body(self, driver: WebDriver) -> str | None:
        try:
            body = driver.execute_cdp_cmd('Network.getResponseBody', {"requestId": self.request_id})['body']
            return body
        except Exception:
            return None


class Requests:
    RESOURCE_T0_IGNORE = [
        ResourceType.IMAGE.value, ResourceType.SCRIPT.value, ResourceType.STYLESHEET.value,
        ResourceType.FONT.value, ResourceType.PING.value
    ]

    def __init__(self):
        self.data = {}

    def add_request(self, step_key: str, request: Request) -> None:
        if step_key not in self.data:
            self.data[step_key] = [request]
        else:
            self.data[step_key].append(request)

    def add_response(self, driver: WebDriver, response: Response, metrics: Metrics, step_name: str) -> None:
        for step_key, requests_list in self.data.items():
            if response.request_id in requests_list:
                index = requests_list.index(response.request_id)
                request = requests_list[index]
                body = response.get_body(driver) or ''
                if response.status >= 400 or '"meta":{"status":"failure"' in body:
                    response.has_error = True
                    request.payload = request.get_payload(driver)
                    response.body = body
                request.response = response

                metrics.record_metric(
                    'response_time',
                    int((response.timestamp - request.timestamp) * 1000),
                    {'url': response.url, 'status': response.status, 'step': step_name,
                     'alt_time': response.receive_headers_end - response.request_time,
                     'response_time': response.response_time, 'request_time': request.timestamp,
                     'response_request_time': response.request_time, 'header_time': response.receive_headers_end}
                )
                return

        request = EmptyRequest()
        request.response = response
        if 'only_response' not in self.data:
            self.data['only_response'] = [request]
        else:
            self.data['only_response'].append(request)

    def __get_responses_without_request(self) -> list[EmptyRequest] | None:
        data = self.data.get('only_response')
        if data:
            del self.data['only_response']
        return data

    def log_browser(self, driver: WebDriver, logger: Logger, step_key: str, step_name: str):
        types = ['browser', 'performance', 'driver']
        for log_type in types:
            browser_messages = driver.get_log(log_type)
            for message in browser_messages:
                logger.debug(f"StepKey: {step_key}, StepName: {step_name}, {log_type} Message: {message}")

    def from_logs(self, driver: WebDriver, metrics: Metrics, step_key: str, step_name: str)\
            -> tuple[list[Request] | None, list[EmptyRequest] | None]:
        messages = driver.get_log('performance')

        for message in messages:
            message_json = json.loads(message['message'])
            message_details_json = message_json.get('message')
            if not message_details_json:
                return None, None
            elif message_details_json['params'].get('type') in self.RESOURCE_T0_IGNORE:
                continue

            if message_details_json['method'] == "Network.requestWillBeSent":
                request = Request(message_details_json['params'])
                self.add_request(step_key, request)
            elif message_details_json['method'] == "Network.responseReceived":
                response = Response(message_details_json['params'])
                self.add_response(driver, response, metrics, step_name)

        return self.data.get(step_key), self.__get_responses_without_request()
