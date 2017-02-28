# home_slack_runner
Python slackbot to tie in various home automation devices and provide control and feedback via slack


## Why did you make this bot?

I recently went on holiday but I wanted to be sure that my internet connected devices could be accessed, controlled and monitored from outside my network. The problem was that I didn't want to open an easily exploitable route into my home network, potentially opening me to attacks. I'd been writing a slackbot for work and I'd really enjoyed it, so I decided to let Slack handle my authentication and NAT traversal. 

## Why not a web interface?
Home-assistant already exists and is better than anything I could write, plus as above, I really like having Slack handle all the fiddly network bits and authentication.

## How does it work?
I use everyone else's hard work with the slackclient, phue and python-nest modules and then wrap them in my code to let me control my house from anywhere my phone can get internet. The trigger word is configurable, but because I am a massive Iron Man fan, I went with Jarvis, thus I can do things like 
`Jarvis Hue bedroom status`
which returns something like
`Lights in the bedroom are OFF` 


## So you only do two things?
At the moment, I'm going to try and add more to it as I get time, things like chromecast control, Alexa integration so I can shout at my computer and make things happen, a dream of programmers since time immemorial. Profanity might even skip error handling to make things faster, who knows?

## How do I install it? 
You're going to need Python 3.6 installed, clone this repo and then start a virtualenv with `--python=python3.6` as an argument then activate the virtual environment and `pip install -r requirements.txt` Yes, it's a bit clunky at the moment. 

Before you start the bot you'll need to fill out the config.json which tells the bot what to load and what to access, along with your credentials. If you're using nest, you'll need to get a secret and a product id from a nest dev account from https://developers.nest.com/

You'll also need a slack you can access, probably best to make it one of your own, you can start your own slack at https://slack.com/ and then make a bot and get a key using https://api.slack.com/custom-integrations and going through the `Listen for and respond to messages with a bot user` section. 

By default it will let _anyone_ on the slack do whatever they like to your house. You can choose an authorised user using your user's slack ID to limit this. This is strongly recommended
