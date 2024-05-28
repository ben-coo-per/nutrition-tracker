# Apple Health GPT-4 Nutrition Tracker Shortcut
Quick project that uses Apple Shortcuts to log an estimate of the macros in a description of food. I find this extremely lightweight approach to be much more intuitive than using a 3rd party app to handle logging or, god forbid, logging it manually. If you have an Iphone and want to get your own version up and running, it's quite simple to set up (I'd estimate no more than 15min if you aren't familiar with Apple Shortcuts, less if you are).
[server based on fast api railway starter template](https://github.com/railwayapp-templates/fastapi/)


## 🥞Stack

- FastAPI
- [Hypercorn](https://hypercorn.readthedocs.io/)
- OpenAI GPT-4o

## 👩‍💻 Running Locally

- Install packages with pip using `pip install -r requirements.txt`
- Add your `OPENAI_API_KEY` to an `.env` file in the root dir ([Get key here](https://platform.openai.com/api-keys))
- Run locally using `hypercorn main:app --reload`

## 🚀 Deploying

I used Railway to deploy this, which is extremely easy to do.
It should be already set up OOTB, so all you have to do is:

- Clone this repo
- [Create a new (free) Railway project](https://railway.app/new) that points to that github repo
- 🙌 boom! you're done

## 📲 Hooking it up to your iPhone (Apple Shortcut)

1. Deploy the API
2. [Give your Service a public domain](https://docs.railway.app/guides/public-networking#railway-provided-domain)
3. Save [this Apple Shortcut](https://www.icloud.com/shortcuts/9d1ec337508d4a0fa7b73175157f76b0)
4. Update the URL in the first action block to match the public domain from step 2 (make sure it's in the format https://{YOUR_PATH}.up.railway.app/)
5. Go through the Health Log Action blocks below individually and provide write access to Shortcuts.
6. 🙌 All done! It's now ready to run - you can also save it to your homescreen as a widget 😊

## 📝 Extra Notes

- To learn about how to use FastAPI with most of its features, you can visit the [FastAPI Documentation](https://fastapi.tiangolo.com/tutorial/)
- To learn about Hypercorn and how to configure it, read their [Documentation](https://hypercorn.readthedocs.io/)
