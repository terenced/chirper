from django.core.management.base import NoArgsCommand, CommandError
from django.core import management
import os.path

class Command(NoArgsCommand):

    help = "clears the db, runs a syncdb, and then generates auth tokens for all the users"

    def handle_noargs(self, **options):
        if os.path.exists('chirper.db'):
            print 'flushing db'
            management.call_command('flush', verbosity=0, interactive=False)
        else:
            print 'syncing db'
            management.call_command('syncdb', verbosity=0, interactive=False)

        print 'generating user tokens'
        management.call_command('gentokens', verbosity=0, interactive=False)

