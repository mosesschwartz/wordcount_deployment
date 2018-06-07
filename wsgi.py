from wordcount import wordcount
app = wordcount.app
app.config['SWAGGER_BASEPATH'] = '/'

if __name__ == "__main__":
    app.run()

