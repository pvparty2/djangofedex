def handle_uploaded_file(f):
    filename = r"C:\Users\pvparty2\Desktop\Hobbies\Coding\Languages\Python\personal_projects\2021 01 01\django\fedex\djangofedex\fedexapp\banners\hello.txt"
    with open(filename, 'w') as destination:
        destination.write('hello')