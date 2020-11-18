@echo off
echo Creating data directory
mkdir data
echo Running scraper
py gsocscraper/scraper.py
echo Data files created at the "data/" route