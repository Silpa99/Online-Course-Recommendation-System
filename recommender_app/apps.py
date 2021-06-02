from django.apps import AppConfig


class RecommenderAppConfig(AppConfig):
    name = 'recommender_app'

    def ready(self):
        import recommender_app.signals
