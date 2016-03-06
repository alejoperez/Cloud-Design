import celeryApp
from hello.models import Administrator, Design, Designer
from hello.src import imageUtils, emailUtils


@celeryApp.app.task
def updateInProgressDesigns():
    designQS = Design.objects.filter(status=1)
    designList = list(designQS)
    for design in designList:
        imageUtils.resizeImage(design)
        design.status=2
        design.save()
        emailUtils.sendMailImageProccesed(design.designer.email)