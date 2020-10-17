from deneme_flask import app

'''
# When you deploy this app into openshift as a container, uncomment following commands.
# This will take ip address of the container and run the app.
# Will prevent wrong loopback

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)



if __name__ == '__main__':
    app.run(debug=True,host="{}".format(IPAddr))
'''

if __name__ == '__main__':
    app.run(debug=True,host="localhost")
    
