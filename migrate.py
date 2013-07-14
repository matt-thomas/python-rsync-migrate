#/usr/bin/env python

import os
from optparse import OptionParser
from migration_data import *

parser = OptionParser()

parser.add_option('-s', action="store", dest="backup_server",
    help="type string", default="all")

options, args = parser.parse_args()


def run_file_migration(name):
   
    for migration in FILE_MIGRATIONS:
        if name == migration['host'] or name == 'all':
            excludes = ''
            for exclude in migration['exclude']:
                excludes = '%s --exclude=%s' % (excludes, exclude)
            rsync_command = 'rsync -rlv %s %s@%s:%s %s' % (excludes, migration['user'], migration['host'], migration['remote_dir'], migration['local_dir'])
            os.system(rsync_command)
                
if __name__ == '__main__':
    run_file_migration(options.backup_server)

