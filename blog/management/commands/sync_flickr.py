from django.core.management.base import NoArgsCommand
from lawrencetrailhawks.lib.syncer import sync_flickr

class Command(NoArgsCommand):
    
    def handle(self, **options):
        print "Syncing flickr BITCHES!!..."
        sync_flickr()
        print "Done!"