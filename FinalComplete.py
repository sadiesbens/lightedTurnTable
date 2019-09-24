import maya.cmds as mc
import random
import OptionsWindowBaseClass

'''Mercedes JAMES
Final
This program will generate a turntable with 3 directional
lights pointing at the center. It also creates a camera that is
animated to revolve around the center with a liner tangent'''

class Turntable(OptionsWindowBaseClass.OptionsWindow):
    def __init__(self): 
        OptionsWindowBaseClass.OptionsWindow.__init__(self)
        self.title = "TurntableTool" 
        self.actionCmd()  
        
        
    def displayOptions(self):
        self.myLayout = mc.rowColumnLayout(adjustableColumn=True)
        self.textInput1 = mc.text(label ='Please slect color and  type light intensity')
        
        '''This create the checkbox options'''
        self.light = mc.text(label='Choose Light to adjust')
        self.turnOnLight1 = mc.checkBox(label = "Key Light")
        self.turnOnLight2 = mc.checkBox(label = "Fill Light")
        self.turnOnLight3 = mc.checkBox(label = "Rim Light")
        
        
        '''This creats the floatfield that lets you input a number 
        for the intensity of the lights'''
        self.light= mc.floatField()

        self.button1 = mc.button(label='Apply intensity', command= self.ChooseIntensity)
        
        '''This create the colorpicker'''
        self.colors = mc.colorInputWidgetGrp()
        mc.button(label='Apply Color', command= self.ChooseColor)
        
    def actionCmd(self, *args):
    
        #create turntable        
        mc.polyCylinder(h=0.223, r=6.44)
        #create lights
        self.light1=mc.directionalLight()
        mc.xform(t=(2.265,6.358,-6.81), ro=(-139.31,-12.398,31.896))  
        self.light2=mc.directionalLight()  
        mc.xform( t=(7.9,7.7,0),ro=(-71.7,22.8,-41.0))
        self.light3=mc.directionalLight()
        mc.xform(t=(-2.3,7.1,7.5), ro=(-43.9,-12.4,31.9))
        
        self.animateCam()
       

    def animateCam(self):
        #create Camera
        self.cam=mc.camera()
        mc.xform(t=(-30.89,9.5,2.3),ro=(-14.3,-83.4,0))
        grp=mc.group(w=False, a=False, r=False)
        #rotate camera
        
        mc.move(0,0,0, grp+".rotatePivot", absolute= True)
        #animation
        
        mc.currentTime(0)
        mc.setKeyframe(grp, at ="rotateY", v =0)
        mc.currentTime(120)
        mc.setKeyframe(grp, at ="rotateY", v =360)
        
        #change tangent of camera animation to linar
        cmds.keyTangent(  inTangentType='linear', outTangentType='linear' )
    
    #select lights that were picked in the checkbox
       
    def selectLight(self, *args):
        mc.select(clear=True)
        if mc.checkBox(self.turnOnLight1, q=True, v=True):
            mc.select(self.light1, add = True)
        if mc.checkBox(self.turnOnLight2, q=True, v=True):
            mc.select(self.light2, add = True)
        if mc.checkBox(self.turnOnLight3, q=True, v=True):
            mc.select(self.light3, add = True)
 
 
     #selects light and applys color
    def ChooseColor(self,*args):
        self.selectLight()
        obj=mc.ls(sl=True) 
        rgbVal = mc.colorInputWidgetGrp(self.colors, q = True, rgb = True)
        for colorLight in obj:
            mc.setAttr(colorLight+'.colorR',rgbVal[0])
            mc.setAttr(colorLight+'.colorG',rgbVal[1])
            mc.setAttr(colorLight+'.colorB',rgbVal[2])
         
         #selects light and applys number to intensity       
    def ChooseIntensity(self,*args):
        self.selectLight()
        obj=mc.ls(sl=True) 
        inten = mc.floatField(self.light, q = True, v = True)
        for lights in obj:
            mc.setAttr(lights+'.intensity',inten)      
    

myGUI = Turntable()
myGUI.create()
