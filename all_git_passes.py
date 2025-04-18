from all_in_for import  userid, passid, gitid, gitpass, gitreponame, workflowname
from old_all_in_for import  olduserid, oldpassid, oldgitid, oldgitpass, oldgitreponame, oldworkflowname


gitdashboard = "https://github.com/dashboard"
gitnew = "https://github.com/new"
gitprofie = "https://github.com/"+gitid
giturl = "https://github.com/"
gitlogurl = "https://github.com/login"
gitblankfile = giturl+gitid+"/"+gitreponame+"/"+"new/mqin"
dokereponame = "dockerfile"
newfiereponame = "newtest.py"
seting = giturl+oldgitid+"/"+oldgitreponame+"/"+"settings"
crreateanewblankworkflow = giturl+gitid+'/'+gitreponame+'/new/main?filename=.github%2Fworkflows%2F'+workflowname+'.yml&workflow_template=blank'

docke1 = '''FROM ubuntu:22.04

RUN apt-get update && apt-get install -y \\
    software-properties-common \\
    && add-apt-repository ppa:xtradeb/apps \\
    && apt-get update \\
    && apt-get install -y \\
    ungoogled-chromium \\
    chromium-chromedriver \\
    libnss3 \\
    libgbm1 \\
    libatk-bridge2.0-0 \\
    libgtk-3-0 \\
    libx11-xcb1 \\
    libxcomposite1 \\
    libxdamage1 \\
    libxrandr2 \\
    libxss1 \\
    libxtst6 \\
    libxshmfence1 \\
    python3-pip \\
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install selenium webdriver-manager beautifulsoup4

COPY . /app

WORKDIR /app

'''
