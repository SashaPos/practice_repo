#!/bin/bash
#CodeCademy task
#Script allows to copy all files except of 'secretinfo.md' from 'source' directory to 'build'
#Practicing using loops
echo "Build script welcomes you stranger!"
firstline=$(head -n 1 source/changelog.md)
read -a splitfirstline <<< $firstline
version=${splitfirstline[1]}
echo $version
echo "If you need to change the version and exit script, enter '0'. Enter '1' to continue."
read versioncontinue
if [ $versioncontinue -eq 1 ]
then
  for file in source/*
  do
    if [ $file == "source/secretinfo.md" ]
    then
      echo "$file wouldn't be copied.'"
    else
      echo "$file is being copied."
      cp $file build/
    fi
  done
  cd build/
  echo -e "Version: $version\n'build' contents:"
  ls
  cd ..
  pwd
  ls
else
  echo "Please come back when you are ready"
fi
