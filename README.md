# hcaptcha-solver

## Say GoodBye to Paid Hcaptcha Solvers.
### Since Qin2dim repo is back. I will archieve this repo.
I modified two already available codes at github and made this captcha solver. Check out the [references](https://github.com/kokiez/hcaptcha-solver#ai-captcha-solver-reference).
Rather than opening a browser and solving hcaptcha, this code **sovles hcaptcha by sending requests**. This way you will get the captcha_key or token easily.

## Installation
- Run the file named **install_requirements.bat**, it will install all the necessary `requirements` for this code.
- Run the file named **Download_Update.bat**, it will download all the `models for the ai captcha solver` and also update the labels in `modules>ai_finder>objects.yaml` file.
- you need a chromedriver. Based on your chrome version:
       Goto your chrome installation folder, usually its installed in `C:\Program Files\Google\Chrome\Application`. You must find a folder named something like this 105.0.5195.127, it can be different for you. Thats your chrome version. 
	   Goto [chrome driver download](https://chromedriver.chromium.org/downloads "chrome driver download") and download your chrome driver. Paste it in **data** folder.
- **Optional:** You need some good **proxies** for the requests sent. You can find them at [proxy scrapper](https://github.com/kokiez/hcaptcah-proxy-scraper-checker "proxy scrapper"). It wills scrap proxies for hcaptcha site. Add the proxies to **proxies.txt file** in **data folder**. **Format IP:PORT**
- To test the captcha solver, Run the file named **run_program.bat**.


## Important piece of code
`from modules.captcha import CaptchaSolver`

`from modules.console import Console`

`token = CaptchaSolver.get_captcha_by_ai("4c672d35-0701-42b2-88c3-78380b0db560", "http://discord.com" ,"1.1.1.1:8080")`

### Issues or great ideas to improve code
1. [FAQS](https://github.com/kokiez/hcaptcha-solver/issues?q=is%3Aissue+is%3Aclosed)
2. If you got a great idea to improve this code, pull a request or hit me up on discord

### Want to Improve Models?
**How to:** Text official owner of the Ai Captcha Solver, Link to pypi project: **[Click me](https://pypi.org/project/hcaptcha-challenger/)**.

**Fact:** Nothing is Perfect.

**Detail of Fact:** No matter how many times you improve the models, hcaptcha will add another single picture and your hours of hardwork/perfect solver will be gone to waste. So, when you got a free working hcaptcha solver and not paying a penny, why improve them?.

### Errors you might get:
1. **Max ssl error**, i have no idea how to solve it rather than putting a time.sleep at line 127 before making request in `modules > hcaptcha > challenges.py`

### Some Proofs
Solves captcha in 10 Seconds.
![success_test1](https://user-images.githubusercontent.com/105941365/190708068-4bb95bdd-b6a2-41a6-9e9b-244cdc69c181.png)

------------

![success_test2](1.png)

------------

![success_test3](2.png)

------------

![success_test4](3.png)

------------

### Reason why i started working on this project ?
I used many paid api's capmonster, anti-captcha, bought from github users, All of them had solving time of 15 to 30 seconds. Every one claims we are coming with a v2 update, then scams you!. Some sell outdated codes, and if you ask why it takes time. They ask you to Buy HQ proxies from them.

### Ai Captcha Solver Reference:
I modifed a couple of github codes. The fastest one i could come across was by [QIN2DIM](https://github.com/QIN2DIM/hcaptcha-challenger  "this one"). 
His/her models dont have enough images, But still it works alot better than others. 

Looks like QIN2DIM repo got ripped off github's face. But his/her project on [pypi](https://pypi.org/project/hcaptcha-challenger/) helped getting back those models and bringing this project alive.

### Hcaptcha Requests Reference:
For sure one thing i knew that the code used in [this repo](https://github.com/imvast/Discord-Account-Creator  "this repo") wasn't his work. 
Looking at the code, Its a piece of art which will stay forever on walls of github and good amount of hardwork done on getting **each element** of the requests made by hcaptcha. 

Someone from github reached out to me and shared info about the [real author](https://github.com/h0nde/  "real author") whose repo has been deleted off github due to which i won't be able to reference to his work but found the [orginal repo](https://github.com/AcierP/py-hcaptcha  "orginal repo")  which identified as **h0nde** work. More info about h0nde can be found [here](https://www.reddit.com/r/discordapp/comments/nuz8jj/so_h0nde_has_made_an_account_using_your_email/).


### Contributions:
- Assigning images to variable rather than downloading and storing them on disk: [MaxAndolini](https://github.com/MaxAndolini "MaxAndolini")

## Donations:

1. **Bitcoin Address:** `1CaR49e4YnsqUALxsSds7PeyZhiDBpussK` Network: `Bitcoin`
2. **USDT Address:** `TQCdnhXQHmKSgR2z4nmGMPGovR36V5XMLp` Network: `Trc20`
3. **BUSD Address:** `0xe9c9effb32da72f3bb28fb102c5497046ab9a59d` Network: `BEP20`
