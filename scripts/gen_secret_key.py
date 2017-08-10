#!/usr/bin/env python

import random


SECRET_KEY = ''.join([random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50)])
#secret = file(SECRET_FILE, 'w')
#secret.write(SECRET_KEY)
#secret.close()

print "SECRET_KEY = '%s'" % SECRET_KEY
