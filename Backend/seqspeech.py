
import qi
import time
import sys
import argparse

Sentences=["stand up",
            "sit down",
            "lie on belly",
            "lie on back",
            "move forward",
            "move backward",
            "turn left",
            "turn right",
            "open left hand",
            "open right hand",
            "close left hand",
            "close right hand",
            "blow kiss",
            "macarena",
            "push ups",
            "that is enaugh"]


class seqVoicRecog(object):

    def __init__(self, app,Nao):
        self.code=""
        self.exit=False
        self.Nao=Nao       
        self.app=app
        self.app.start()
        session = self.app.session
        # Get the service ALMemory.
        self.memory = session.service("ALMemory")
        # Get the services ALTextToSpeech and ALFaceDetection.
        self.voice_reco = session.service("ALSpeechRecognition")
        self.voice_reco.setLanguage("English")

    
    def onLoad(self):
        from threading import Lock
        self.bIsRunning = False
        self.mutex = Lock()
        self.hasPushed = False
        self.voice_reco.hasSubscribed = False


    def onInput_onStart(self):    
        self.voice_reco.pause(True)
        self.mutex.acquire()
        if(self.bIsRunning):
            self.mutex.release()
            return
        self.bIsRunning = True
        try:
            if self.voice_reco:
                self.voice_reco.setVisualExpression(True)
                self.voice_reco.pushContexts()
            self.hasPushed = True
            self.voice_reco.setVocabulary( Sentences, True )
            self.subscriber = self.memory.subscriber("WordRecognized")
            self.subscriber.signal.connect(self.on_human_tracked)
            self.voice_reco.subscribe("SeqVoicRecog")
            self.voice_reco.hasSubscribed = True
            self.Nao.say("you can order me now")
        except RuntimeError, e:
            self.mutex.release()
            self.onUnload()
            raise e
        self.mutex.release()
        self.voice_reco.pause(False)

    def on_human_tracked(self, value):
        self.voice_reco.pause(True)
        print 'word recognized'
        if(len(value) > 1 and value[1] >= 0.3):
            print 'recognized the word :', str(value)
            if (value[0]=="<...> stand up <...>"):
                if(self.code==""):
                    self.Nao.say("Ok first I will stand up")
                else:
                    self.Nao.say("then I will stand up")
                self.code += "self.Nao.stand()\n"
            elif (value[0]=="<...> sit down <...>"):
                if(self.code==""):
                    self.Nao.say("Ok first I will sit down")
                else:
                    self.Nao.say("then I will sit down")
                self.code += "self.Nao.sit()\n"
            elif (value[0]=="<...> crouch <...>"):
                if(self.code==""):
                    self.Nao.say("Ok first I will crouch")
                else:
                    self.Nao.say("then I will crouch")
                self.code += "self.Nao.crouch()\n"
            elif (value[0]=="<...> lie on belly <...>"):
                if(self.code==""):
                    self.Nao.say("Ok first I will lie on belly")
                else:
                    self.Nao.say("then I will lie on belly")
                self.code += "self.Nao.LyingBelly()\n"
            elif (value[0]=="<...> lie on back <...>"):
                if(self.code==""):
                    self.Nao.say("Ok first I will lie on back")
                else:
                    self.Nao.say("then I will lie on back")
                self.code += "self.Nao.LyingBack()\n"
            elif (value[0]=="<...> move forward <...>"):
                if(self.code==""):
                    self.Nao.say("Ok first I will move forward")
                else:
                    self.Nao.say("then I will move forward")
                self.code += "self.Nao.walk(20,0)\n"
            elif (value[0]=="<...> move backward <...>"):
                if(self.code==""):
                    self.Nao.say("Ok first I will move backward")
                else:
                    self.Nao.say("then I will move backward")
                self.code += "self.Nao.walk(-20,0)\n"
            elif (value[0]=="<...> turn left <...>"):
                if(self.code==""):
                    self.Nao.say("Ok first I will turn left")
                else:
                    self.Nao.say("then I will turn left")
                self.code += "self.Nao.turn(90)\n"
            elif (value[0]=="<...> turn right <...>"):
                if(self.code==""):
                    self.Nao.say("Ok first I will turn right")
                else:
                    self.Nao.say("then I will turn right")
                self.code += "self.Nao.turn(-90)\n"
            elif (value[0]=="<...> open left hand <...>"):
                if(self.code==""):
                    self.Nao.say("Ok first I will close my left hand")
                else:
                    self.Nao.say("then I will close my left hand")
                self.code += "self.Nao.OpenHand('LHand')\n"
            elif (value[0]=="<...> open right hand <...>"):
                if(self.code==""):
                    self.Nao.say("Ok first I will open my right hand")
                else:
                    self.Nao.say("then I will open my right hand")
                self.code += "self.Nao.OpenHand('RHand')\n"
            elif (value[0]=="<...> close left hand <...>"):
                if(self.code==""):
                    self.Nao.say("Ok first I will close my left hand")
                else:
                    self.Nao.say("then I will close my left hand")
                self.code += "self.Nao.CloseHand('LHand')\n"
            elif (value[0]=="<...> close right hand <...>"):
                if(self.code==""):
                    self.Nao.say("Ok first I will close my right hand")
                else:
                    self.Nao.say("then I will close my right hand")
                self.code += "self.Nao.CloseHand('RHand')\n"
            elif (value[0]=="<...> say <...>"):
                if(self.code==""):
                    self.Nao.say("Ok first I will say Hello World")
                else:
                    self.Nao.say("then I will say Hello World")
                self.code += "self.Nao.say('Hello World')\n"
            elif (value[0]=="<...> wave <...>"):
                if(self.code==""):
                    self.Nao.say("Ok first I will wave")
                else:
                    self.Nao.say("then I will wave")
                self.code += "self.Nao.wave()\n"
            elif (value[0]=="<...> wipe <...>"):
                if(self.code==""):
                    self.Nao.say("Ok first I will wipe")
                else:
                    self.Nao.say("then I will wipe")
                self.code += "self.Nao.wipeForehead()\n"
            elif (value[0]=="<...> bow <...>"):
                if(self.code==""):
                    self.Nao.say("Ok first I will bow")
                else:
                    self.Nao.say("then I will bow")
                self.code += "self.Nao.bow()\n"
            elif (value[0]=="<...> blow kiss <...>"):
                if(self.code==""):
                    self.Nao.say("Ok first I will give blow kiss")
                else:
                    self.Nao.say("then I will give blow kiss")
                self.code += "self.Nao.blowkiss()\n"
            elif (value[0]=="<...> macarena <...>"):
                if(self.code==""):
                    self.Nao.say("Ok first I will do macrena dance")
                else:
                    self.Nao.say("then I will do macrena dance")
                self.code += "self.Nao.macrenadance()\n"
            elif (value[0]=="<...> push ups <...>"):
                if(self.code==""):
                    self.Nao.say("Ok first I will do pushups")
                else:
                    self.Nao.say("then I will do pushups")
                self.code += "self.Nao.pushups()\n"
            elif (value[0]=="<...> blink <...>"):
                if(self.code==""):
                    self.Nao.say("Ok first I will blink")
                else:
                    self.Nao.say("then I will blink")
                self.code += "self.Nao.blink()\n"
            elif (value[0]=="<...> that is enaugh <...>"):
                if(self.code==""):
                    self.Nao.say("Ok, as you like")
                else:
                    self.Nao.say("let's start")
                exec(self.code)
                self.code=""
                self.onUnload()
                self.app.stop()
                self.exit=True
                self.subscriber=None
            time.sleep(1)
        else:
            print 'unsifficient threshold'
        self.voice_reco.pause(False)
         
    def onUnload(self):
        self.voice_reco.pause(True)
        self.mutex.acquire()
        try:
            if (self.bIsRunning):
                if (self.voice_reco.hasSubscribed):
                    self.voice_reco.unsubscribe("SeqVoicRecog")
                if (self.hasPushed and self.voice_reco):
                    self.voice_reco.popContexts()
        except RuntimeError, e:
            self.mutex.release()
            raise e
        self.bIsRunning = False
        self.mutex.release()
        self.voice_reco.pause(False)


    def run(self):
        print "Starting VoicRecog"
        self.onLoad()
        self.onInput_onStart()
        try:
            while (self.exit==False):
                time.sleep(1)
                self._is_running = False
            print("done stopping VoicRecog")
        except KeyboardInterrupt:
            print "Interrupted by user, stopping VoicRecog"
            #stop
            self.onUnload()
            sys.exit(0)


