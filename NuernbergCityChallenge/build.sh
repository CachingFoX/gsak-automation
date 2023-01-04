#!/bin/zsh
rm -f NuernbergCityChallenge.gskz
rm -f build.log

cp gskz.prototype NuernbergCityChallenge.gskz
zip -r NuernbergCityChallenge.gskz NuernbergCityChallenge.gsk >>build.log
cd assets
zip -r ../NuernbergCityChallenge.gskz * >>../build.log
cd ..
unzip -l NuernbergCityChallenge.gskz >>build.log
