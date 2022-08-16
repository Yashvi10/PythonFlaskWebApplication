#!/bin/bash
sudo apt install git
sudo apt -y update
sudo apt -y upgrade
git clone https://github.com/Yashvi10/WebApp

cd WebApp
sudo npm install
sudo npm start