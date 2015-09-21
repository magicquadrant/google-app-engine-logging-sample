#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import logging
from google.appengine.api import taskqueue


class MainHandler(webapp2.RequestHandler):
    def get(self):
        logging.info('Log Message from MainHandler')
        taskqueue.add(url='/testmeget', method='GET')
        taskqueue.add(url='/testmepost')
        self.response.write('Hello world!')


class TestMeGetHandler(webapp2.RequestHandler):
    def get(self):
        logging.info('Log Message from TestMeGetHandler')
        self.response.set_status(204)


class TestMePostHandler(webapp2.RequestHandler):
    def post(self):
        logging.info('Log Message from TestMePostHandler')
        self.response.set_status(204)


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/testmeget', TestMeGetHandler),
    ('/testmepost', TestMePostHandler),
], debug=True)
