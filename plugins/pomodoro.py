from twisted.words.protocols import irc
from twisted.internet import protocol
from twisted.internet import reactor
import bot

class Pomodoro():
    """A pomodoro timer."""
    def __init__(self):
        pomodoros = []
        commands = {"start": self.pomodoro_start,
                    "clear": self.clear_pomodoros}
    def pomo(self):
        pass

    def send_table(self, target):
        """Send a register table to the user or channel specified by target."""
        # IMPLEMENT

    def add_pomodoro(self, split):
        """Add a pomodoro to the stack.
        Keyword arguments:
            split | A tuple of the form (working, break) where working is how many
                    minutes you will spend working and break is how many minutes
                    are in the break.
        """
        if split[0] + split[1] > 60: return # UNFINISHED BUT NEEDS TO BE HANDLED

        if self.pomodoros:
            self.pomodoros.insert(0, split)
        else:
            self.pomodoros.append(split)

    def pomodoro_break(self):
        """Pull current pomodoro from stack and start the break period of a pomodoro."""
        split = self.pomodoros.pop()
        break_ = split[1]
        # IMPLEMENT: However we want to wait X minutes for the break
        self.pomodoro_start()

    def pomodoro_start(self):#
        """Start the next pomodoro on the stack."""
        print "foo"
        # IMPLEMENT: Schedule an event working minutes in the future for pomodoro
        # to end at and break to start.


    def send_pomodoros(self, target):
        """Send a list of pomodoros on the stack to the user or channel specified by target."""
        # IMPLEMENT

    def clear_pomodoros(self):
        """Clear all pomodoros on the stack besides the current one."""
        for pomodoro in self.pomodoros:
            if pomodoro is not self.pomodoros[0]:
                self.pomodoros.remove(pomodoro)

class PomodoroRegister():
    """A register table for users in channel to register their project to the timer with."""
    def __init__(self):
        self.working = {}
    
    def register(self, user, task):
        """Register a user as working on task for this Pomodoro."""
        self.working[user] = task
        # IMPLEMENT: Send back a confirmation to the user who registered.
        # IDEA: Perhaps limit the length of the string a user can use to describe their pomodoro?
    
    def working_on(self, user):
        """Return the task that a user is registered as working on."""
        return self.working[user]
    
    def get_table(self):
        """Return the entire table of user:task pairs."""
        return self.working
