class Meme:
    def __init__(self, topic, meta=None):
        if meta is None:
            self.topic = topic
        else:
            self.topic = '{topic}: \'{meta}\''.format(topic=topic, meta=meta.topic)
    
    def __str__(self):
        return 'Topic: {}'.format(self.topic)

def complain(meme)        :
    complaint = Meme(topic='complaining about', meta=meme)
    print(complaint)
    complain(complaint)

if __name__ == '__main__':
    complain(Meme('What is stopping you from coding like this?'))
