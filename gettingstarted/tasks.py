import celeryApp
from hello.models import Administrator, Design, Designer
from hello.src import ImageUtils, EmailUtils


@celeryApp.app.task
def updateInProgressDesigns():
    designQS = Design.objects.filter(status=1)
    designList = list(designQS)
    for design in designList:
        ImageUtils.resizeImage(design)
        design.status=2
        design.save()
        EmailUtils.sendMailImageProccesed(design.designer.email)
