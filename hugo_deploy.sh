# GitHub A records
# 192.30.252.153
# 192.30.252.154
#!/bin/bash
#*
# rm -rf public
# git submodule add -b master https://github.com/taikii/whiteplain.git themes/whiteplain
# git submodule add -b master https://github.com/InTEGr8or/hugo_blackplain_theme.git themes/blackplain
# git clone https://gist.github.com/aad5b14b17276e803d352898a6c88c5b.git tmp
# mv hugo_deploy.sh .
# rm -rf tmp/

printf "\033[0;32mDeploying updates to GitHub...\033[0m"

# printf "Build the project."
# rmdir docs/** -r
rm -rf docs

printf "Building Hugo"
hugo 
baseURL=$(cat config.toml | grep baseURL | awk '{print $3}' | tr -d \")
printf $baseURL > docs/CNAME

msg="rebuilding site `date`"
if [ $# -eq 1 ]
  then msg="$1"
fi

cd themes/blackplain
git add .
git commit -m "$msg"
git pull
git push
# return to parent folder
cd ../..
git add themes/blackplain

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
# read
# open $baseURL
