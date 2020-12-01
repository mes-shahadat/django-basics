from django.apps import AppConfig


class DjsignalConfig(AppConfig):
    name = 'djsignal'
    def ready(self):
        import djsignal.signals
