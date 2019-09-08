# -*- coding: utf-8 -*-
from seqArabicSpeech import seqArabicVoicRecog
import qi
import time
import sys
import argparse

Sentences=["قف",
            "إجلس",
            "انحنى",
            "أرقد على صدرك",
            "أرقد على ظهرك",
            "تحرك للأمام",
            "تحرك للخلف",
            "أتجه لليسار",
            "أتجه لليمين",
            "افتح يدك اليسرى",
            "افتح يدك اليمنى",
            "اغلق يدك اليسرى",
            "اغلق يدك اليمنى",
            "قل أهلاً وسهلاً",
            "لوح",
            "امسح",
            "تحية",
            "قبلة هواية",
            "ماكارينا",
            "ضغط",
            "وميض"]

SeqSentences=["قف",
            "إجلس",
            "انحنى",
            "أرقد على صدرك",
            "أرقد على ظهرك",
            "للأمام",
            "للخلف",
            "أتجه لليسار",
            "أتجه لليمين",
            "افتح يدك اليسرى",
            "افتح يدك اليمنى",
            "اغلق يدك اليسرى",
            "اغلق يدك اليمنى",
            "قل أهلاً وسهلاً",
            "لوح",
            "امسح",
            "تحية",
            "قبلة هواية",
            "ماكارينا",
            "ضغط",
            "وميض",
            "يكفي"]

class ArVoicRecog(object):

    def __init__(self, app,Nao):
        self.Nao=Nao
        self.exit=False
        super(ArVoicRecog, self).__init__()
        self.app=app
        self.code=""
        app.start()
        session = app.session
        # Get the service ALMemory.
        self.memory = session.service("ALMemory")
        # Get the services ALTextToSpeech and ALFaceDetection.
        self.voice_reco = session.service("ALSpeechRecognition")
        self.sensmemory = session.service("ALMemory")
        self.subscriber1 = self.sensmemory.subscriber("TouchChanged")
        self.subscriber1.signal.connect(self.onTouched)
        self.voice_reco.setLanguage("Arabic")
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
                self.Nao.say("حسناً، انتظر حتى أفتحُ مفكرتي لأُسَجل ما تريد")
                self.run_seq()
            if p[0]=='Head/Touch/Rear' and p[1]==True:
                print('Head/Touch/Rear')
                self.exitmain=False
                self.app.stop()
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
            self.voice_reco.subscribe("ArVoicRecog")
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
            self.Nao.say("حسناً، أنا مستعد الأن")
            self.subscriber = self.memory.subscriber("WordRecognized")
            self.subscriber.signal.connect(self.on_human_tracked_seq)
            self.voice_reco.subscribe("ArSeqVoicRecog")
            self.voice_reco.hasSubscribed = True
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
            if (value[0]=="<...> قف <...>"):
                if(self.code==""):
                    self.Nao.say("حسناً، فى البداية تُريدٌني أن أقف")
                else:
                    self.Nao.say("ثم سأقف")
                self.code += "self.Nao.stand()\n"
            elif (value[0]=="<...> إجلس <...>"):
                if(self.code==""):
                    self.Nao.say("حسناً، فى البداية تُريدُني أن أجلس")
                else:
                    self.Nao.say("ثم سأجلس")
                self.code += "self.Nao.sit()\n"
            elif (value[0]=="<...> انحنى <...>"):
                if(self.code==""):
                    self.Nao.say("حسناً، فى البداية تُريدٌني أن انحني")
                else:
                    self.Nao.say("ثم سانحني")
                self.code += "self.Nao.crouch()\n"
            elif (value[0]=="<...> أرقد على صدرك <...>"):
                if(self.code==""):
                    self.Nao.say("حسناً، فى البداية تُريدٌني أن أرقُد على صدري")
                else:
                    self.Nao.say("ثم سأرقٌد على صدري")
                self.code += "self.Nao.LyingBelly()\n"
            elif (value[0]=="<...> أرقد على ظهرك <...>"):
                if(self.code==""):
                    self.Nao.say("حسناً، فى البداية تُريدٌني أن أرقُد على ظهري")
                else:
                    self.Nao.say("ثم سأرقٌد على ظهري")
                self.code += "self.Nao.LyingBack()\n"
            elif (value[0]=="<...> للأمام <...>"):
                if(self.code==""):
                    self.Nao.say("حسناً، فى البداية تُريدٌني أن أتحرك للأمام")
                else:
                    self.Nao.say("ثم سأتحرك للأمام")
                self.code += "self.Nao.walk(20,0)\n"
            elif (value[0]=="<...> للخلف <...>"):
                if(self.code==""):
                    self.Nao.say("حسناً، فى البداية تُريدٌني أن أتحرك للخلف")
                else:
                    self.Nao.say("ثم سأتحرك للخلف")
                self.code += "self.Nao.walk(-20,0)\n"
            elif (value[0]=="<...> أتجه لليسار <...>"):
                if(self.code==""):
                    self.Nao.say("حسناً، فى البداية تُريدٌني أن أتجه لليسار")
                else:
                    self.Nao.say("ثم سأتجه لليسار")
                self.code += "self.Nao.turn(90)\n"
            elif (value[0]=="<...> أتجه لليمين <...>"):
                if(self.code==""):
                    self.Nao.say("حسناً، فى البداية تُريدٌني أن أتجه لليمين")
                else:
                    self.Nao.say("ثم سأتجه لليمين")
                self.code += "self.Nao.turn(-90)\n"
            elif (value[0]=="<...> افتح يدك اليسرى <...>"):
                if(self.code==""):
                    self.Nao.say("حسناً، فى البداية تُريدٌني أن افتح يدي اليسرى")
                else:
                    self.Nao.say("ثم سأفتح يدي اليسرى")
                self.code += "self.Nao.OpenHand('LHand')\n"
            elif (value[0]=="<...> افتح يدك اليمنى <...>"):
                if(self.code==""):
                    self.Nao.say("حسناً، فى البداية تُريدٌني أن افتح يدي اليمنى")
                else:
                    self.Nao.say("ثم سأفتح يدي اليمنى")
                self.code += "self.Nao.OpenHand('RHand')\n"
            elif (value[0]=="<...> اغلق يدك اليسرى <...>"):
                if(self.code==""):
                    self.Nao.say("حسناً، فى البداية تُريدٌني أن اغلق يدي اليسرى")
                else:
                    self.Nao.say("ثم سأغلق يدي اليسرى")
                self.code += "self.Nao.CloseHand('LHand')\n"
            elif (value[0]=="<...> اغلق يدك اليمنى <...>"):
                if(self.code==""):
                    self.Nao.say("حسناً، فى البداية تُريدٌني أن اغلق يدي اليمنى")
                else:
                    self.Nao.say("ثم سأغلق يدي اليسرى")
                self.code += "self.Nao.CloseHand('RHand')\n"
            elif (value[0]=="<...> قل أهلاً وسهلاً <...>"):
                if(self.code==""):
                    self.Nao.say("حسناً، فى البداية تُريدٌني أن اقل أهلاً وسهلا")
                else:
                    self.Nao.say("ثم سأقول أهلاً وسهلاً")
                self.code += "self.Nao.say('Hello World')\n"
            elif (value[0]=="<...> لوح <...>"):
                if(self.code==""):
                    self.Nao.say("حسناً، فى البداية تُريدٌني أن الوح بيدي")
                else:
                    self.Nao.say("ثم سأُلوح بيدي")
                self.code += "self.Nao.wave()\n"
            elif (value[0]=="<...> امسح <...>"):
                if(self.code==""):
                    self.Nao.say("حسناً، فى البداية تُريدٌني أن امسح رأسي")
                else:
                    self.Nao.say("ثم سأمسح رأسي")
                self.code += "self.Nao.wipeForehead()\n"
            elif (value[0]=="<...> تحية <...>"):
                if(self.code==""):
                    self.Nao.say("حسناً، فى البداية تُريدٌني أن اللقى تحية")
                else:
                    self.Nao.say("ثم سأُلقي التحية")
                self.code += "self.Nao.bow()\n"
            elif (value[0]=="<...> قبلة هواية <...>"):
                if(self.code==""):
                    self.Nao.say("حسناً، فى البداية تُريدٌني أن اعطي قبلة هواية")
                else:
                    self.Nao.say("ثم سأُعطي قبلة هواية")
                self.code += "self.Nao.blowkiss()\n"
            elif (value[0]=="<...> ماكارينا <...>"):
                if(self.code==""):
                    self.Nao.say("حسناً، فى البداية تُريدٌني أن ارقٌص ماكارينا")
                else:
                    self.Nao.say("ثم سأرقٌص ماكارينا")
                self.code += "self.Nao.macrenadance()\n"
            elif (value[0]=="<...> ضغط <...>"):
                if(self.code==""):
                    self.Nao.say("حسناً، فى البداية تُريدٌني أن أؤدى ضغط")
                else:
                    self.Nao.say("ثم سأؤدى ضغط")
                self.code += "self.Nao.pushups()\n"
            elif (value[0]=="<...> وميض <...>"):
                if(self.code==""):
                    self.Nao.say("حسناً، فى البداية تُريدٌني أن اجعل عيني تومض")
                else:
                    self.Nao.say("ثم سأجعل عيني تومض")
                self.code += "self.Nao.blink()\n"
            self.voice_reco.pause(False)
            if (value[0]=="<...> يكفي <...>"):
                self.voice_reco.pause(True)
                if(self.code==""):
                    self.Nao.say("حسناً، كما تشاء")
                else:
                    self.Nao.say("هيا نبدأ")
                exec(self.code)
                self.code=""
                self.onUnload()
                self.app.stop()
                self.exit=True
                self.subscriber=None
            time.sleep(2)
        else:
            print 'unsifficient threshold'
        

    def on_human_tracked(self, value):
        print 'word recognized'
        self.voice_reco.pause(True)
        if(len(value) > 1 and value[1] >= 0.3):
            print 'recognized the word :', str(value)
            if (value[0]=="قف"):
                self.Nao.stand()
            elif (value[0]=="إجلس"):
                self.Nao.sit()
            elif (value[0]=="انحنى"):
                self.Nao.crouch()
            elif (value[0]=="أرقد على صدرك"):
                self.Nao.LyingBelly()
            elif (value[0]=="أرقد على ظهرك"):
                self.Nao.LyingBack()
            elif (value[0]=="تحرك للأمام"):
                self.Nao.walk(20,0)
            elif (value[0]=="تحرك للخلف"):
                self.Nao.walk(-20,0)
            elif (value[0]=="أتجه لليسار"):
                self.Nao.turn(90)
            elif (value[0]=="أتجه لليمين"):
                self.Nao.turn(-90)
            elif (value[0]=="افتح يدك اليسرى"):
                self.Nao.OpenHand("LHand")
            elif (value[0]=="افتح يدك اليمنى"):
                self.Nao.OpenHand("RHand")
            elif (value[0]=="اغلق يدك اليسرى"):
                self.Nao.CloseHand("LHand")
            elif (value[0]=="اغلق يدك اليمنى"):
                self.Nao.CloseHand("RHand")
            elif (value[0]=="قل أهلاً وسهلاً"):
                self.Nao.say("أهلاً وسهلا")
            elif (value[0]=="لوح"):
                self.Nao.wave()
            elif (value[0]=="امسح"):
                self.Nao.wipeForehead()
            elif (value[0]=="تحية"):
                self.Nao.bow()
            elif (value[0]=="قبلة هواية"):
                self.Nao.blowkiss()
            elif (value[0]=="ماكارينا"):
                self.Nao.macrenadance()
            elif (value[0]=="ضغط"):
                self.Nao.pushups()
            elif (value[0]=="وميض"):
                self.Nao.blink()
            time.sleep(5)
        else:
            print 'unsifficient threshold'
        self.onUnload()
        self.app.stop()
        self.exit=True
        self.subscriber=None
         
    def onUnload(self):
        self.voice_reco.pause(True)
        self.mutex.acquire()
        try:
            if (self.bIsRunning):
                if (self.hasSubscribed):
                    self.voice_reco.unsubscribe("ArVoicRecog")
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



  
