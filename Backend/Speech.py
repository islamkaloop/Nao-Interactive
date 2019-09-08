from seqspeech import seqVoicRecog
import qi
import time
import sys
import argparse

Sentences=["stand up",
            "sit down",
            "crouch",
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
            "say",
            "wave",
            "wipe",
            "bow",
            "blow kiss",
            "macarena",
            "push ups",
            "blink"]

SeqSentences=["stand up",
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

class VoicRecog(object):

    def __init__(self, app,Nao):
        self.Nao=Nao
        self.exit=False
        super(VoicRecog, self).__init__()
        self.app=app
        self.code=""
        self.app.start()
        session = self.app.session
        # Get the service ALMemory.
        self.memory = session.service("ALMemory")
        # Get the services ALTextToSpeech and ALFaceDetection.
        self.voice_reco = session.service("ALSpeechRecognition")
        self.sensmemory = session.service("ALMemory")
        self.subscriber1 = self.sensmemory.subscriber("TouchChanged")
        self.subscriber1.signal.connect(self.onTouched)
        self.voice_reco.setLanguage("English")
        self.exitmain=True
        while (self.exitmain):
            time.sleep(1)
    
    def onTouched(self, value):
        """ This will be called each time a touch
        is detected.

        """
        # Unsubscribe to the event when talking,
        # to avoid repetitions
        for p in value:
            if p[0]=='Head/Touch/Front' and p[1]==True:
                print('Head/Touch/Front') 
                self.run()
            if p[0]=='Head/Touch/Middle' and p[1]==True:
                print('Head/Touch/Middle')
                self.Nao.say("Ok, wait till open my ToDo list")
                self.run_seq()
            if p[0]=='Head/Touch/Rear' and p[1]==True:
                print('Head/Touch/Rear')
                self.app.stop()
                self.exitmain=False
                self.subscriber1=None



    def onLoad(self):
        from threading import Lock
        self.bIsRunning = False
        self.mutex = Lock()
        self.hasPushed = False
        self.hasSubscribed = False


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
            self.voice_reco.setVocabulary( Sentences, False )
            self.subscriber = self.memory.subscriber("WordRecognized")
            self.subscriber.signal.connect(self.on_human_tracked)
            self.voice_reco.subscribe("VoicRecog")
            self.hasSubscribed = True
        except RuntimeError, e:
            self.mutex.release()
            self.onUnload()
            raise e
        self.mutex.release()
        self.voice_reco.pause(False)

    def onInput_onStart_seq(self):    
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
            self.voice_reco.setVocabulary( SeqSentences, True )
            self.subscriber = self.memory.subscriber("WordRecognized")
            self.subscriber.signal.connect(self.on_human_tracked_seq)
            self.voice_reco.subscribe("SeqVoicRecog")
            self.voice_reco.hasSubscribed = True
            self.Nao.say("you can order me now")
        except RuntimeError, e:
            self.mutex.release()
            self.onUnload()
            raise e
        self.mutex.release()
        self.voice_reco.pause(False)

    def on_human_tracked_seq(self, value):
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
            self.voice_reco.pause(False)
            if (value[0]=="<...> that is enaugh <...>"):
                self.voice_reco.pause(True)
                if(self.code==""):
                    self.Nao.say("Ok, as you like")
                else:
                    self.Nao.say("let's start")
                exec(self.code)
                self.code=""
                self.onUnload()
                #self.app.stop()
                self.exit=True
                self.subscriber=None
            time.sleep(1)
        else:
            print 'unsifficient threshold'
        
       
    def on_human_tracked(self, value):
        self.voice_reco.pause(True)
        print 'word recognized'
        if(len(value) > 1 and value[1] >= 0.3):
            print 'recognized the word :', str(value)
            if (value[0]=="stand up"):
                self.Nao.stand()
            elif (value[0]=="sit down"):
                self.Nao.sit()
            elif (value[0]=="crouch"):
                self.Nao.crouch()
            elif (value[0]=="lie on belly"):
                self.Nao.LyingBelly()
            elif (value[0]=="lie on back"):
                self.Nao.LyingBack()
            elif (value[0]=="move forward"):
                self.Nao.walk(20,0)
            elif (value[0]=="move backward"):
                self.Nao.walk(-20,0)
            elif (value[0]=="turn left"):
                self.Nao.turn(90)
            elif (value[0]=="turn right"):
                self.Nao.turn(-90)
            elif (value[0]=="open left hand"):
                self.Nao.OpenHand("LHand")
            elif (value[0]=="open right hand"):
                self.Nao.OpenHand("RHand")
            elif (value[0]=="close left hand"):
                self.Nao.CloseHand("LHand")
            elif (value[0]=="close right hand"):
                self.Nao.CloseHand("RHand")
            elif (value[0]=="say"):
                self.Nao.say("Hello")
            elif (value[0]=="wave"):
                self.Nao.wave()
            elif (value[0]=="wipe"):
                self.Nao.wipeForehead()
            elif (value[0]=="bow"):
                self.Nao.bow()
            elif (value[0]=="blow kiss"):
                self.Nao.blowkiss()
            elif (value[0]=="macarena"):
                self.Nao.macrenadance()
            elif (value[0]=="push ups"):
                self.Nao.pushups()
            elif (value[0]=="blink"):
                self.Nao.blink()
            time.sleep(5)
        else:
            print 'unsifficient threshold'
        self.onUnload()
        #self.app.stop()
        self.exit=True
        self.subscriber=None
         
    def onUnload(self):
        self.voice_reco.pause(True)
        self.mutex.acquire()
        try:
            if (self.bIsRunning):
                if (self.hasSubscribed):
                    self.voice_reco.unsubscribe("VoicRecog")
                if (self.hasPushed and self.voice_reco):
                    self.voice_reco.popContexts()
        except RuntimeError, e:
            self.mutex.release()
            raise e
        self.bIsRunning = False
        self.mutex.release()
        self.voice_reco.pause(False)


    def run_seq(self):
        print "Starting VoicRecog"
        self.onLoad()
        self.onInput_onStart_seq()
        try:
             while (self.exit==False):
                time.sleep(1)
                self._is_running = False
        except KeyboardInterrupt:
            print "Interrupted by user, stopping VoicRecog"
            #stop
            self.onUnload()
            sys.exit(0)

    def run(self):
        print "Starting VoicRecog"
        self.onLoad()
        self.onInput_onStart()
        try:
             while (self.exit==False):
                time.sleep(1)
                self._is_running = False
        except KeyboardInterrupt:
            print "Interrupted by user, stopping VoicRecog"
            #stop
            self.onUnload()
            sys.exit(0)


