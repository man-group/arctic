import optparse
import pymongo
import uuid
import base64
import sys

from ..auth import get_auth, authenticate
from ..hooks import get_mongodb_uri


def main():
    usage = """usage: %prog [options] username ...

    Create the user's personal Arctic database, and adds them, read-only
    to the central admin database.
    """

    parser = optparse.OptionParser(usage=usage)
    parser.add_option("--host", default='localhost', help="Hostname, or clustername. Default: localhost")
    parser.add_option("--password",dest="password", default=None, help="Password. Default: random")
    parser.add_option("--admin-write", dest="admin", action='store_false', default=True,
                      help="Give write access to the admin DB. Default: False")
    parser.add_option("--dryrun", "-n", dest="dryrun", action="store_true", help="Don't really do anything", default=False)
    parser.add_option("--verbose", "-v", dest="verbose", action="store_true", help="Print some commentary", default=False)
    parser.add_option("--nodb", dest="nodb", help="Don't create a 'personal' database", action="store_true", default=False)

    (opts, args) = parser.parse_args()

    c = pymongo.MongoClient(get_mongodb_uri(opts.host))
    credentials = get_auth(opts.host, 'admin', 'admin')
    if not credentials:
        print >>sys.stderr, "You have no admin credentials for instance '%s'" % (opts.host)
        return

    if not authenticate(c.admin, credentials.user, credentials.password):
        print >>sys.stderr, "Failed to authenticate to '%s' as '%s'" % (opts.host, credentials.user)
        return

    for user in args:

        p = opts.password

        if p is None:
            p = base64.b64encode(uuid.uuid4().bytes).replace('/', '')[:12]

        if not opts.dryrun:
            if opts.verbose:
                print "Adding user %s to DB %s" % (user, opts.host)
            if not opts.nodb:
                if opts.verbose:
                    print "Adding database arctic_%s to DB %s" % (user, opts.host)
                c['arctic_' + user].add_user(user, p)
            c.admin.add_user(user, p, read_only=opts.admin)
        else:
            print "DRYRUN: add user %s readonly %s nodb %s" % (user, opts.admin, opts.nodb)

        if not opts.password:
            print "%-16s %s" % (user, p)

if __name__ == '__main__':
    main()
