from django.shortcuts import render
from .models import *
import aspose.words as aw
from django.db.models import Max
from docx2pdf import convert
from pdf2docx import parse
from typing import Tuple
import moviepy.editor as me
import speech_recognition as sr

def convert_pdf2docx(input_file: str, output_file: str, pages: Tuple = None):
    """Converts pdf to docx"""
    if pages:
        pages = [int(i) for i in list(pages) if i.isnumeric()]
    result = parse(pdf_file=input_file,
                   docx_with_path=output_file, pages=pages)
    summary = {
        "File": input_file, "Pages": str(pages), "Output File": output_file
    }
    # Printing Summary
    print("## Summary ########################################################")
    print("\n".join("{}:{}".format(i, j) for i, j in summary.items()))
    print("###################################################################")
    return result

# Create your views here.
def home(request):
    return render(request,"home.html")
def word2pdf(request):
    context={'file':''}
    if request.method=="POST":
        file=request.FILES['wrd']
        requestnumber=reqtno.objects.aggregate(Max('requestnumber'))
        obj = files(req=requestnumber['requestnumber__max']+1,fl=file)
        obj.save()
        reqtno.objects.all().delete()
        newreq=reqtno(requestnumber=requestnumber['requestnumber__max']+1)
        newreq.save()
        obj=files.objects.all().filter(req=requestnumber['requestnumber__max']+1)
        convert("media\{}".format(obj[0].fl),"media\{}.pdf".format(obj[0].fl))
        context={'file':obj}
        return render(request,'word2pdf.html',context)
    else:
        return render(request,'word2pdf.html',context)

def pdf2word(request):
    if request.method=="POST":
        file=request.FILES['pdf']
        requestnumber=reqtno.objects.aggregate(Max('requestnumber'))
        obj = files(req=requestnumber['requestnumber__max']+1,fl=file)
        obj.save()
        reqtno.objects.all().delete()
        newreq=reqtno(requestnumber=requestnumber['requestnumber__max']+1)
        newreq.save()
        obj=files.objects.all().filter(req=requestnumber['requestnumber__max']+1)
        convert_pdf2docx(input_file="media\{}".format(obj[0].fl),output_file="media\{}.docx".format(obj[0].fl))
        filename=""
        for i in range(0,len(str(obj[0].fl))):
            if str(obj[0].fl)[i]==".":
                break
            else:
                filename+=str(obj[0].fl)[i]
        filename={"filename":filename}
        context={'file':filename}
        return render(request,'pdf2word.html',context)
    else: 
        return render(request,"pdf2word.html")

def video2audio(request):
    if request.method=="POST":
        filename=request.FILES['video']
        otformat=request.POST['output']
        requestnumber=reqtno.objects.aggregate(Max('requestnumber'))
        obj = videofiles(req=requestnumber['requestnumber__max']+1,fl=filename,otformat=otformat)
        obj.save()
        reqtno.objects.all().delete()
        newreq=reqtno(requestnumber=requestnumber['requestnumber__max']+1)
        newreq.save()
        obj=videofiles.objects.all().filter(req=requestnumber['requestnumber__max']+1)
        video=me.VideoFileClip("media\{}".format(obj[0].fl))
        audio=video.audio
        audio.write_audiofile("media\{}{}".format(obj[0].fl,otformat))
        context={'file':obj}
        return render(request,"video2audio.html",context)
    else:
        return render(request,"video2audio.html")
    
def speech2text(request):
    if request.method=="POST":
        audio=request.FILES['audio']
        requestnumber=reqtno.objects.aggregate(Max('requestnumber'))
        requestnumber=requestnumber['requestnumber__max']+1
        files(req=requestnumber,fl=audio).save()
        reqtno.objects.all().delete()
        reqtno(requestnumber=requestnumber).save()
        obj=files.objects.all().filter(req=requestnumber)
        recognize=sr.Recognizer()
        with sr.AudioFile("media\{}".format(obj[0].fl)) as source:
            audio_data=recognize.record(source)
        text=recognize.recognize_google(audio_data,language="en-us")
        file=open("media\{}.txt".format(obj[0].fl),'w')
        file.write(text)
        file.close()
        context={"file":obj}
        return render(request,"audio2text.html",context)
    else:
        return render(request,"audio2text.html")
    
def pagenotfound(request,exception):
    return render(request,"404.html",status=404)