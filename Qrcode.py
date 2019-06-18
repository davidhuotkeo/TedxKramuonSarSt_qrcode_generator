# IMPORT LIBRARIES
import qrcode
import six

# CREATE QRCODE CLASS
class QRcode(object):
    def __init__(self, qr_object):
        # QROBJECT
        self.qr_object = qr_object
        # EXTENSIONS
        self.ext = ['png', 'bmp', 'jpeg', 'jpg']

    # PUT DATA TO THE QRCODE FOR GENERATION
    def input_data(self, data):
        # IF IT IS STRING OR INTEGER MAKE IT ELSE WRONG DATATYPE
        if isinstance(data, int) or isinstance(data, six.string_types):
            self.qr_object.add_data(data)
            self.qr_object.make(fit=True)
        else:
            print('Wrong data type only integer or string')

    # GENERATE PICTURE
    # FILENAME CAN USE WITH PATH
    def generate(self, filename, extension, path=''):
        # IF THE EXTENSION IS INCLUDED IN ARRAY OF EXTENSION
        if extension in self.ext:
            img = self.qr_object.make_image()
            # SAVE IMAGE
            if path == '':
                img.save('{}.{}'.format(filename, extension))
            else:
                if path[-1] == '/':
                    path = path[:-1]
                    img.save('{}/{}.{}'.format(path, filename, extension))

# EXAMPLE
# CREATE QR_OBJECT
qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=20,
        border=1,
    )

q = QRcode(qr)
q.input_data('David is awesome')
q.generate('david', 'png')
