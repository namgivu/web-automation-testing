#!/usr/bin/env bash

#                              q aka show only container id, a aka show all
seleniumContainers="docker ps -qa
                              -f name=selenium-hub
                              -f name=selenium-node-ch
                              -f name=selenium-node-ff
"
docker stop    $($seleniumContainers)
docker rm   -f $($seleniumContainers)

# docker rm -f $(docker ps -qa) #remove all when needed
