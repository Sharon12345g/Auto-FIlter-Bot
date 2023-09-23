if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/XO-NOVA/KING-STEVE.git /KING-STEVE
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /KING-STEVE
fi
cd /KINGSTEVEBot
pip3 install -U -r requirements.txt
echo "Bot Assembilng...."
python3 bot.py
