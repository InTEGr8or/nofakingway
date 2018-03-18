# GitHub A records
# 192.30.252.153
# 192.30.252.154
#!/bin/bash
#*
# rm -rf public
# git submodule add -b master git@github.com:InTEGr8or/nofakingway.git public
# git submodule add -b master git@github.com:InTEGr8or/hugo_blackplain_theme.git layouts

printf "\033[0;32mDeploying updates to GitHub...\033[0m"

printf "Build the project."
rmdir docs/** -r
rm -rf docs/** 

printf "nofakingway.com" > docs/CNAME
hugo # if using a theme, replace with `hugo -t <YOURTHEME>`

msg="rebuilding site `date`"
if [ $# -eq 1 ]
  then msg="$1"
fi

# Go To layouts/ 
cd layouts
git add .
git commit -m "$msg"
git pull
git push
# return to parent folder
cd ..

# Add changes to git.
git add .
# Commit changes.
git commit -m "$msg"

git pull
# Push source and build repos.
git push # origin master -f

# Come Back up to the Project Root
# cd ..

printf "Task complete. You may close this window..."
read
# open "http://nofakingway.com"