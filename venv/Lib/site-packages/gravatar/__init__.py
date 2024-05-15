# gravatar.py
# Author: Jake Voytko <jakevoytko@gmail.com>
# Time-stamp: <2010-02-06 12:55:57 jake>

'''Generates a Gravatar from an email. Calling...

    gravatar.make('jakevoytko@gmail.com')

returns the valid Gravatar image:

    http://gravatar.com/avatar/2145579130b5dd2aaa367501de04273c

Optional parameters:

 * rating:  One of 'g', 'pg','r', or 'x'. These carry the same meaning as
            their MPAA counterparts.
 * size:    A number satisfying 1<=number<=512.
 * default: Either a URL that returns a default image, or a 'special
            value'. Special values are one of 'identicon', 'monsterid',
            'wavatar', or '404'. This field is not checked for validity.

 'ValueError' or 'TypeError' will be raised when invalid parameters
 are detected, depending on the offense'''

import urllib
import hashlib


def make(email, rating=None, size=None, default=None):
    '''Generates a Gravatar image URI using 'email'. See the module
    documentation for usage information.'''
    if not _PurposelyString(email):
        raise TypeError('Email type invalid: ' + type(email))

    baseUrl = 'http://gravatar.com/avatar/'
    emailHash = hashlib.md5(email.lower()).hexdigest()
    args={}

    if rating is not None:
        if not _PurposelyString(rating):
            raise TypeError('Bad rating type: %s' % type(rating))

        rating = str(rating).lower()
        if rating not in ['g','pg','r','x']:
            raise ValueError('Invalid Gravatar rating: %s' % rating)
        args['r'] = rating

        
    if size is not None:
        size=int(size)
        if not (1 <= size <= 512):
            raise ValueError('Invalid Gravatar size: %s Must be 1<=size<=512'
                             %size)
        args['s'] = size

        
    if default:
        args['d'] = str(default)

        
    ret = baseUrl + emailHash
    if len(args):
        ret += '?' + urllib.urlencode(args)

    return ret


def _PurposelyString(s):
    '''Checks to see if 's' is either a str or a unicode object.'''
    return isinstance(s, str) or isinstance(s, unicode)

# Copyright 2010 Jake Voytko. All rights reserved.

# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:

#    1. Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.

#    2. Redistributions in binary form must reproduce the above
#       copyright notice, this list of conditions and the following
#       disclaimer in the documentation and/or other materials
#       provided with the distribution.

# THIS SOFTWARE IS PROVIDED BY <COPYRIGHT HOLDER> ``AS IS'' AND ANY
# EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
# PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL <COPYRIGHT HOLDER> OR
# CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF
# USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT
# OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
# SUCH DAMAGE.

# The views and conclusions contained in the software and
# documentation are those of the authors and should not be interpreted
# as representing official policies, either expressed or implied, of
# Jake Voytko.
