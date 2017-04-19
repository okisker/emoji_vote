# emoji_vote
Vote on your favorite emoji using Venmo

What you need to use this program:
- A Venmo account
- A Gmail account
- A Plot.ly account

## Set Up Venmo

Make sure the gmail you are using for this project is the email assigned to that Venmo account.

## Set Up Gmail

Email:
Add the email that is assigned to the Venmo account on line 23:
```
#GMAIL API                            
EMAIL_ACCOUNT = "emoji.test.omkisker@gmail.com"
```

Enable Access for Less Secure Apps:
- Click "My Account":

<img width="341" alt="my account" src="https://cloud.githubusercontent.com/assets/25387083/25189691/e585c380-24f7-11e7-8f8a-3aac564a7fd6.png">

- Security Checkup:

<img width="390" alt="security checkup" src="https://cloud.githubusercontent.com/assets/25387083/25189699/ec9ff6ae-24f7-11e7-9bb0-a7854b991ca8.png">

- Skip down to where it says "Disable Access for Less Secure Apps" and turn it on:

<img width="661" alt="disable access for less secure apps on" src="https://cloud.githubusercontent.com/assets/25387083/25189704/f0de54fe-24f7-11e7-8bd6-de60c8d17123.png">

## Set Up Plot.ly

Username:
Remember your username when you create the account.

API Key:
- Click "Settings":

<img width="173" alt="settings" src="https://cloud.githubusercontent.com/assets/25387083/25190113/4119f7d8-24f9-11e7-85f2-9a56b925adae.png">

- API Keys:

<img width="237" alt="api keys" src="https://cloud.githubusercontent.com/assets/25387083/25190119/46486ad2-24f9-11e7-9e14-8692ac7b22e4.png">

- Regenerate Key:

<img width="599" alt="regenerate key" src="https://cloud.githubusercontent.com/assets/25387083/25190125/4a3af740-24f9-11e7-9a18-a22906cdf196.png">

Replace both the Username and API Key to yours on line 13:
```
plotly.tools.set_credentials_file(username='contactsyracuse', api_key='yPvHRVgh2zfvGgAfpI3c')
```

## Running the Program

When you run the program, it will ask for the Gmail password. Type it in and the plot.ly graph should appear (looks best in full-size).

Good luck fundraising/ voting! Let me know if you have any issues!
