import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import mysql.connector

# Variables that contains the user credentials to access Twitter API
access_token = "360807471-H7imTvf6vXmcT6tDMUT4ps5viUjESmUjYFtX2JTV"
access_token_secret = "S99FCxwyfxaYTPZt8RXRKOGa9s4RWwuodsbN8kgmoVviO"
consumer_key = "QlzHtgh8h1I3XbtDxQULLjQmW"
consumer_secret = "j2eK2xzD0OzdgLaD1VfFaBPHURxK2eQaezBgJzp9HOuTtQ5NBK"

list_hamilton = ["Hamilton Musical", "Hamilton Broadway", "Richard Rodgers Theatre", "Lin Manuel Broadway",
                 "@HamiltonMusical", "@Lin_Manuel broadway", "Hamilton Soundtrack", "Hamilton New York",
                 "Hamilton NYC", "You'll be Back Hamilton", "room where it happens", "Hamilton Theatre",
                 "Hamilton Stage", "#hamiltonbroadway", "#broadwayhamilton", 'Hamilton Review']
list_waitress = ["Waitress Broadway", "She used to be mine", "Brooks Atkinson", "SaraBareilles Waitress",
                 "Waitress Musical", "Jenna Waitress", "Waitress Soundtrack", "Waitress New York", "Waitress NYC",
                 "Waitress Theatre", "Waitress Stage", "Jessie Nelson", "Waitress Adrienne Shelly", "#WaitressMusical",
                 "waitressmusical", "#waitressbroadway", "#WaitressBroadway", "Waitress Review"]
list_prettywoman = ["Pretty Woman Broadway", "Nederlander Theatre", "Samantha Barks Broadway",
                    "@SamanthaBarks Pretty Woman", "@SamanthaBarks broadway", "@PrettyWoman", "#prettywomanmusical",
                    "#prettywomanbroadway", "#PrettyWomanTheMusical", "Pretty Woman the Musical",
                    "Samantha Barks Pretty Woman", "Steve Kazee Pretty Woman", "Bryan Adams Broadway",
                    "Vivian Ward Pretty Woman", "Pretty Woman Musical", "Pretty Woman Soundtrack",
                    "Pretty Woman New York", "Pretty Woman NYC", "Pretty Woman Theatre", "Pretty Woman Stage",
                    "Pretty Woman Review"]
list_generic = ["Broadway", "Broadway Musical", "Musical"]

master_list = list_hamilton + list_waitress + list_prettywoman + list_generic
f = open("Buzz_Data_Final.txt", "w+")


# This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        f.write(data + "\n")
        print(data)
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':
    # This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    while True:
        # This line filter Twitter Streams
        try:
            stream.filter(track=master_list)
        except:
            print("Stream Broken")
            continue



f.close()
