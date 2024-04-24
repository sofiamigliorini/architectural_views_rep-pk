#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Anonymous
Email: Anonymous

This script executes all the steps of dataset creation.
"""
import shutil
import subprocess
from pathlib import Path

if __name__ == "__main__":
    print('\n\n########## Step 0: running query_github script ##########\n')
    subprocess.run(["python3", "-m", "src.dataset_creation.00githubViewExtraction"],
                   cwd=Path(__file__).parent.parent)

    print('\n\n########## Step 1: running filter_multi_dev_dataset script ##########\n')
    subprocess.run(["python3", "-m", "src.dataset_creation.01cleaning"],
                   cwd=Path(__file__).parent.parent)

    print('\n\n########## Step 2: running filter_lifespan_dataset script ##########\n')
    subprocess.run(["python3", "-m", "src.dataset_creation.02filter"],
                   cwd=Path(__file__).parent.parent)

    print('\n\n########## Step 3: running detect_dc_dataset script ##########\n')
    subprocess.run(["python3", "-m", "src.dataset_creation.03imageCommitsExtraction"],
                   cwd=Path(__file__).parent.parent)
    
    print('\n\n########## Step 4: running detect_dc_dataset script ##########\n')
    subprocess.run(["python3", "-m", "src.dataset_creation.04imageCommitsAnalysis"],
                   cwd=Path(__file__).parent.parent)
    
    print('\n\n########## Step 5: running detect_dc_dataset script ##########\n')
    subprocess.run(["python3", "-m", "src.dataset_creation.05sampling"],
                   cwd=Path(__file__).parent.parent)

   
   
