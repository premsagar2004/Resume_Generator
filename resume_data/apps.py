from django.apps import AppConfig


class ResumeDataConfig(AppConfig):
    name = 'resume_data'

    def ready(self):
        import resume_data.signals
