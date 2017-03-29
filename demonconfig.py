import sys, time


class SigFunctionsCon:
    def __init__(self, ourdaemon):
        self.__ourdaemon = ourdaemon

    def SIGTERM(self):
        sys.stderr.write("process was stopped!\n")
        sys.exit(0)
        return


class ReactFunctionCon:
    def __init__(self, ourdaemon):
        self.__ourdaemon = ourdaemon

    def start(self):
        self.__ourdaemon.start()

    def stop(self):
        self.__ourdaemon.stop()

    def restart(self):
        self.__ourdaemon.restart()

    def stmess(self, message):
        print(message)
        self.__ourdaemon.start()


class StatCon:
    strHelp = "Autmation has be applied to distribution sistem feeder for a long time, aspecially as related to " \
              "protection and the restoration of some parts of the feeder. "

    def run(self):
        while (True):
            time.sleep(1)

    pidFile = "/tmp/test-daemon.pid"

    inputter = "/dev/null"

    outputter = "/dev/null"

    errorer = "/var/logs/lid"
