#!/bin/bash

echo "If you want to:
- decompress - enter \"1\" or \"decompress\" (without quotes);
- create a gzip archive - enter \"2\" or \"gzip\";
- create a bz2 archive - enter \"3\" or \"bz2\";
- create a xz archive - enter \"4\" or \"xz\"."

read -p "User input: " user_choice

if [ "$user_choice" == "1" ] || [ "$user_choice" == "decompress" ];
then
echo "decompress"
read -p "Enter archive name (name.tar*): " archive_name
read -p "Enter path to target directory: " target_directory
tar xvf $archive_name -C $target_directory
echo "Archive decompressed" && ls $target_directory

elif [ "$user_choice" == "2" ] || [ "$user_choice" == "gzip" ];
then
echo "gzip"
read -p "Enter path to file: " path
cd $path
pwd
ls
read -p "Enter file name: " file_name
read -p "Enter archive name: " gzip_name
tar zcvf $gzip_name $file_name

elif [ "$user_choice" == "3" ] || [ "$user_choice" == "bz2" ];
then
echo "bz2"
read -p "Enter path to file: " path
cd $path
pwd
ls
read -p "Enter file name: " file_name
read -p "Enter archive name: " bz2_name
tar jcvf $bz2_name $file_name

elif [ "$user_choice" == "4" ] || [ "$user_choice" == "xz" ];
then
echo "xz"
read -p "Enter path to file: " path
cd $path
pwd
ls
read -p "Enter file name: " file_name
read -p "Enter archive name: " xz_name
tar Jcvf $xz_name $file_name

fi
