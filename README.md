<!--
 * @Author: Jiagang Chen
 * @Date: 2021-12-08 03:11:55
 * @LastEditors: Jiagang Chen
 * @LastEditTime: 2021-12-08 03:20:03
 * @Description: 
 * @Reference: 
-->

# AT4GCP

This repo is an annotation tool for Ground Control Point, which is modified from opensfm, removing the dependence of opensfm.

## How to install it

    cd AT4GCP/
    pip install -r requirements.txt 

## How to use it

For example, if we use data sample:

    cd AT4GCP/
    python main.py data/berlin

## About Data Structure
You should have a directory and its data structure should be like this:

    - Data Root
      - Images
        - Seq1
        - Seq2
        - Seq3
        - ...
      - ground_control_points.json

That's OK