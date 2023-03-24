from datetime import datetime



def dining_image_upload_path(self, instance):
    filebase, extension = instance.split('.')
    return "dining/{}/{}_{}.{}"\
            .format(self.dining.pk,
                    filebase, 
                    datetime.now().timestamp(),
                    extension) 

