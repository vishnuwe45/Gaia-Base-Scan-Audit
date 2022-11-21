from gaiasdk import sdk
import logging
import time
import subprocess
import os
import git
    
def RunWeakCiperScan(args):
    logging.info("WEAK CIPER scan has been started!")
    logging.info("WEAK CIPER scan has been finished!")
    logging.info("==================================================")

def RunSecurityHeadersScan(args):
    logging.info("SECURITY HEADERS scan has been started!")
    logging.info("SECURITY HEADERS scan has been finished!")
    logging.info("==================================================")

def RunSqlMapScan(args):
    logging.info("SQLMAP scan has been started!")
    logging.info("SQLMAP scan has been finished!")
    logging.info("==================================================")

def RunDirectoryBrutforceScan(args):
    logging.info("DIRECORY BRUTFORCE scan has been started!")
    logging.info("DIRECORY BRUTFORCE scan has been finished!")
    logging.info("==================================================")
    
def main():
    logging.basicConfig(level=logging.INFO)
    runweakciperscan = sdk.Job("Run Weak Ciper Scan", "Runnning Weak Ciper Scan", RunWeakCiperScan)
    runsecurityheadersscan = sdk.Job("Run Security Headers Scan", "Running Security Headers Scan", RunSecurityHeadersScan,["Run Weak Ciper Scan"])
    runsqlmapscan = sdk.Job("Run Sql Map Scan", "Running Sql Map Scan", RunSqlMapScan,["Run Security Headers Scan"])
    rundirectorybrutforcescan = sdk.Job("Run Directory Brutforce Scan", "Running Directory Brutforce Scan", RunDirectoryBrutforceScan, ["Run Sql Map Scan"])
    sdk.serve([runweakciperscan, runsecurityheadersscan, runsqlmapscan, rundirectorybrutforcescan])
