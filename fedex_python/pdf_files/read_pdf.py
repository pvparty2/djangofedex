"""Read the Banner Page from a PDF file and store client information in banners dictionary."""

class BannerPage():
    """Model a Banner Page."""

    def __init__(self, filename):
        """Initialize a Banner Page and its banners variable."""
        self.filename = filename
        self.populate_banners() # Populate self.banners variable.

    def populate_banners(self):
        import PyPDF2, re, pprint
        from .banner_template import banner_template
        
        # Extract text from Banner Page of PDF file.
        with open(self.filename, 'rb') as f:
            pdf_reader = PyPDF2.PdfFileReader(f)
            page_obj = pdf_reader.getPage(0) # Banner Page is the first page of PDF file.
            text = page_obj.extractText()

        # Delete header and footer information.
        text = text[text.index('Banner Page'):] 

        # Separate text by new lines.
        # Do not capture new lines.
        text_re = re.compile(r'(?:\n)([\S ]*)')

        # results is a list of banner keys and banner values
        results = text_re.findall(text)

        # Assign values from PDF text to the keys in 'banners' dictionary.
        self.banners = banner_template

        for i, result in enumerate(results):

            # Break out of for loop if iterating over last element.
            if i + 1 == len(results):
                break

            # Assign banner value to a key in banners dictionary.
            if result in self.banners:
                 value = results[i+1]

                 # If current value is actually a key in banners, skip.
                 if value in self.banners:
                     continue
                    
                # Else add value to the proper key.
                 else:
                    self.banners[result] = value
        
        return self.banners


class Recipient(BannerPage):
    """Model a recipient's attributes for FedEx shipment."""
    
    def __init__(self, filename):
        super().__init__(filename)

        # Recipient name.
        self.f_name = self.banners['Borrower First Name']
        self.l_name = self.banners['Borrower Last Name']
        self.name = f'{self.f_name} {self.l_name}'

        # Recipient address.
        self.address_1 = self.banners['Ship To Address Line 1']
        self.address_2 = self.banners['Ship To Address Line 2']
        self.phone = self.banners['Ship To Address Phone']
        self.attention = self.banners['Ship To Address Attention']
        self.city = self.banners['Ship To Address City']
        self.state = self.banners['Ship To Address State']
        self.zip = self.banners['Ship To Address Zip']
        self.zip_ext = self.banners['Ship To Address Plus4']
