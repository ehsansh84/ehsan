from base_handler import BaseHandler


class SampleClass(BaseHandler):
    def init_method(self):
        self.inputs = {
            'put': ['field1', 'field2', 'field3']
        }


class Setting(BaseHandler):
    def init_method(self):
        self.tokenless = True
        self.inputs = {
            'put': ['ip']
        }

