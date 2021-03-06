__author__ = 'scotm'
import bz2
from subprocess import call

import os
from datetime import datetime
import dropbox
from django.conf import settings
from django.core.management.base import BaseCommand

access_token = u'jdjeIthf6JgAAAAAAAG0_zlvZwIT8hTMkNwnRADwEAlu9kYFQNMeF5AVO4a37GSx'


class Command(BaseCommand):
    help = "Dumps DB to Drobox"

    def handle(self, *args, **options):
        client = dropbox.client.DropboxClient(access_token)
        now = datetime.now().strftime('%Y-%m-%d')
        db_name = settings.DATABASES['default']['NAME']
        filename = 'canvassing_db_%s.pgsql' % now
        with open(filename, 'wb') as myfile:
            call(["pg_dump", db_name], stdout=myfile)
        print "Dump complete - compressing."
        call(["bzip2", filename])
        filename += ".bz2"
        print "Database successfully dumped. Uploading to Dropbox."
        with open(filename) as myfile:
            try:
                client.file_create_folder(now)
                print "Creating folder"
            except dropbox.rest.ErrorResponse as e:
                if e.status != 403:
                    raise
            print "Uploading backup file: %s ..." % filename,
            response = client.put_file("%s" % (filename), myfile)
            print " done. %s" % response['size']
        os.unlink(filename)