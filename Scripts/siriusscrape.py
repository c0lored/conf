#!/usr/bin/python
#Sirius Scrapper is used to log the now playing information of a SIRIUS stream
#Copyright (C) Corey Ling
#
#This program is free software; you can redistribute it and/or
#modify it under the terms of the GNU General Public License
#as published by the Free Software Foundation; either version 2
#of the License, or (at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program; if not, write to the Free Software
#Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

import time
import urllib
import re
from optparse import OptionParser
from xml.dom.minidom import parse

class SiriusScrapper(object):
    def __init__(self):
        self.playing = None

    def getNowPlaying(self):
        '''return a dictionary for current song/artist per channel'''
        nowplaying = {}
        url = 'http://www.siriusxm.com/padData/pad_provider.jsp?all_channels=y'
        sirius_xml = parse(urllib.urlopen(url))

        for channels in sirius_xml.getElementsByTagName('event'):
            channel = channels.getElementsByTagName('channelname')[0].firstChild.data
            song = channels.getElementsByTagName('songtitle')[0].firstChild.data
            artist = channels.getElementsByTagName('artist')[0].firstChild.data
            nowplaying[str(channel).strip().lower()] = {'artist': artist, 'song': song}
        sirius_xml.unlink()

        return nowplaying

    def getStreamNowPlaying(self, stream):
        '''return a dictionary of info about whats currently playing'''
        nowplaying = {}
        channel = None
        nowPlayingInfo = self.getNowPlaying()
        if stream in nowPlayingInfo:
            channel = stream
        else:
            for info in nowPlayingInfo:
                #Remove all non letter characters then compare
                cleanInfo = re.sub("[\W]", "", info)
                cleanStream = re.sub("[\W]", "", stream)
                if cleanStream == cleanInfo or cleanStream in cleanInfo:
                    channel = info
                    break

        if channel:
            channel = channel.strip()
            song = nowPlayingInfo[channel]['song']
            artist = nowPlayingInfo[channel]['artist']
            nowplaying['playing'] = song + ', ' + artist
            nowplaying['longName'] = channel.title()
        else:
            nowplaying['playing'] = 'No channel information for stream ' + stream
            nowplaying['longName'] = 'ERROR'

        nowplaying['logfmt'] = '%s %s: %s' % (time.strftime('%y %m|%d %H:%M'),
            nowplaying['longName'], nowplaying['playing'])

        if nowplaying['playing'] != self.playing:
            nowplaying['new'] = True
            self.playing = nowplaying['playing']
        else:
            nowplaying['new'] = False
        return nowplaying

def log(nowplaying, logfile):
    logfd = open(logfile,'a')
    nowplayinglog = nowplaying['logfmt'].encode("utf-8")
    logfd.write("%s\n" % nowplayinglog)
    logfd.close()


usage = "Usage: %prog [options] stream"
parser = OptionParser(usage=usage)
parser.add_option("-f", "--file", dest="filename",
  help="Write now playing to FILE", metavar="FILE")
parser.add_option("-q", "--quiet",
    action="store_false", dest="verbose", default=True,
    help="don't print status messages to stdout")

(options, args) = parser.parse_args()
stream = args[0]
scrapper = SiriusScrapper()

if(options.verbose):
    print "Logging the stream %s" % stream
while True:
    nowplaying = scrapper.getStreamNowPlaying(stream)

    if(nowplaying['new']):
        if(options.filename):
            log(nowplaying, options.filename)

        if(options.verbose):
            print time.strftime('%H:%M' ) + ' - ' + nowplaying['longName'] + ": " + nowplaying['playing']

    try:
        time.sleep(30)
    except KeyboardInterrupt:
        break