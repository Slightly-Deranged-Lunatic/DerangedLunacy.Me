#!/bin/bash
    echo "Deploying Server"

    cd /srv/webpages/DerangedLunacy.Me
    git pull https://github.com/Slightly-Deranged-Lunatic/DerangedLunacy.Me

    echo "Finished deploying"