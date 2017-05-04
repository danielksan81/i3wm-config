#/bin/bash
i3_folder=~/.config/i3
i3status_folder=~/.config/i3status

echo 'Checking config folders...'
if [ ! -d $i3_folder ]; then
  echo 'Creating i3 config folder ...'
  mkdir -p -v $i3_folder
fi
if [ ! -d $i3status_folder ]; then
  echo 'Creating i3status config folder ...'
  mkdir -p -v $i3status_folder
fi

echo 'Installing i3pystatus...'
sudo -E pip3 install i3pystatus netifaces colour pytz

cp -v i3-config $i3_folder/config
cp -v i3status-config $i3status_folder/config
cp -v statusbar.py $i3_folder/
echo 'Reloading and restarting...'
i3-msg reload
i3-msg restart
