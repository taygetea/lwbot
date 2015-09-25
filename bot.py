from twisted.words.protocols import irc
from twisted.internet import protocol
import re
import plugins.pomodoro

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
    """
    < hugaraxia> When a ban is placed by an op, PM the op for a timeframe to remove the ban (accept "10m" or "2h" or "30d"), and then start timer, remove ban when time is up (+random interval to prevent gaming?). If op doesn't reply: Sane default. (5h?) (Perhaps announce ban time, possibly in ##meta:  fuzzy them to "short", "long", "very long" to prevent gaming.)
    7839-07:12 < hugaraxia> When ban is placed, optionally on very long bans: Start a timer for 1hr: Message #lw-meta that ban discussion on <username> is now allowed.
    """
    def privmsg(self, user, channel, msg):
        reload(plugins)
        print irc.parseModes(msg)
        if msg.startswith(self.nickname):
            msg = re.compile(self.nickname + "[:,]* ?", re.I).sub('', msg)
            prefix = "%s: " % (user.split('!', 1)[0], )
            print msg
            built = prefix + msg
            self.msg(self.factory.channel, built)
        else:
            prefix = ''

class Bantimer:

    def __init__(self, op, user, channel):

        self.operator = op
        self.banned = user
        self.channel = channel
    def timer(self):

    def opmsg(self):
        IrcBot.privmsg(self.op, self.channel, "ban " + self.user + "?")

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
    chan = 'bot'  #sys.argv[1]
    reactor.connectTCP('localhost', 6667, IrcBotFactory('#' + chan))
    reactor.run()
