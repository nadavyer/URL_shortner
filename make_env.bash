#!/bin/bash

cd frontend
npm install
npm run build

cd ../backend
python3 -m virtualenv venv
source venv/bin/activate
pip install -r requirements.txt

cd ..