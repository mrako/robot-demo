#!/bin/bash

cd application
bundle install
bundle exec warble
cd ..

mkdir -p robot/server
cp application/deploy/ROOT.war robot/server/

