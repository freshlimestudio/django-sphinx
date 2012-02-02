__author__ = 'igonef'

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Prints generic configuration by template (defined in SPHINX_CONFIG_TEMPLATE)."

    output_transaction = True

    def handle(self, *args, **options):
        from djangosphinx.utils.config import generate_config_from_template
        self.stdout.write(generate_config_from_template())

  