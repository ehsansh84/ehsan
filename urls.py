from handlers.handlers import SampleClass, Setting


url_patterns = [
    ("/", SampleClass, None, "sample_class"),
    ("/setting", Setting, None, "setting"),
]