from handlers.handlers import SampleClass, Setting


url_patterns = [
    ("/v1/", SampleClass, None, "sample_class"),
    ("/v1/setting", Setting, None, "setting"),
]