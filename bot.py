from twisted.words.protocols import irc
from twisted.internet import protocol
import re
import plugins

print plugins.modules

class IrcBot(irc.IRCClient):
    def _get_nickname(self):
        return self.factory.nickname
    nickname = property(_get_nickname)

    def signedOn(self):
        self.join(self.factory.channel)
        print "Signed on as %s." % (self.nickname,)

    def joined(self, channel):
        print "Joined %s." % (channel,)

    def privmsg(self, user, channel, msg):
        reload(plugins)
        if not user:
            return
        if msg.startswith(self.nickname):
            msg = re.compile(self.nickname + "[:,]* ?", re.I).sub('', msg)
            prefix = "%s: " % (user.split('!', 1)[0], )
            evaluated = eval(msg)
            self.msg(self.factory.channel, prefix + str(evaluated))
        else:
            prefix = ''


class IrcBotFactory(protocol.ClientFactory):
    protocol = IrcBot

    def __init__(self, channel, nickname='Elua'):
        self.channel = channel
        self.nickname = nickname
        self.password = "password"

    def clientConnectionLost(self, connector, reason):
        print "Lost connection (%s), reconnecting." % (reason,)
        connector.connect()

    def clientConnectionFailed(self, connector, reason):
        print "Could not connect: %s" % (reason,)

from twisted.internet import reactor

if __name__ == "__main__":
    chan = 'lw-prog'  #sys.argv[1]
    reactor.connectTCP('irc.freenode.net', 6667, IrcBotFactory('#' + chan))
    reactor.run()
